
// Endpoint URL for California Housing price prediction regression model
const housingEndpoint = '';

// Endpoint URL for Named Entity Recognition
const nerEndpoint = '';

// Endpoint URL for PoS tagging and dependency parsing
const parseEndpoint = ''; 

// S3 bucket name for image uploads
const uploadBucketName = '';

// AWS region of the above S3 bucket for image uploads
const bucketRegion = '';

// AWS identity pool ID for uploading images to S3 bucket
const identityPoolId = '';

// Ednpoint URL for image classification with ResNet50 model
const resnet50Endpoint = '';

// Endpoint URL for image classification with Inception V3 model
const inceptionV3Endpoint = '';


var imagePredictionsChart = null;

AWS.config.update({
    region: bucketRegion,
    credentials: new AWS.CognitoIdentityCredentials({
        IdentityPoolId: identityPoolId
    })
});

var s3 = new AWS.S3({
    apiVersion: '2006-03-01',
    params: { Bucket: uploadBucketName }
});

const displacyEnt = new displaCyENT('', {
    container: '#displacy-ent',
    defaultText: '',
    defaultEnts: ['person', 'org', 'date', 'gpe', 'loc']
});

const displacy = new displaCy(parseEndpoint, {
    container: '#displacy-parse',
    format: 'spacy',
    distance: 200,
    offsetX: 100,
    wordSpacing: 25,
    collapsePunct: false,
    collapsePhrase: false,
    bg: '#e8f4fc',
    onStart: function () {
        $('#parse-container').hide();
        $('#displacyParseLoader').show();
    },
    onSuccess: function () {
        $('#displacyParseLoader').hide();
        $('#parse-container').show();
    },
    onError: function (error) {
        console.log('Error:', error);
        $('#displacyParseLoader').hide();
        $('#parse-container').show();
        alert('Error while getting POS and parse tree. Please try again later.');
    }
});

$('#displacyEntLoader').hide();
$('#displacyParseLoader').hide();
$('#housingLoader').hide();
$('#chartLoader').hide();
$(document).foundation();

const allEntities = ['person', 'org', 'gpe', 'norp', 'fac', 'loc', 'product',
    'event', 'work_of_art', 'law', 'language', 'date', 'time',
    'percent', 'money', 'quantity', 'ordinal', 'cardinal'
];

var lastAnalyzedText = "";
var lastNERSpans = [];
var ents = [];

function getNamedEntities() {
    $('#displacyEntLoader').show();
    $('#displacy-ent').hide();

    ents = [];
    $.each(allEntities, function (index, value) {
        var id = '#' + value;
        if ($(id).is(':checked')) {
            ents.push(value);
        }
    });

    var inputText = $('#inputText').val();

    $.ajax({
        type: "POST",
        url: nerEndpoint,
        data: inputText,
        contentType: "text/plain",
        dataType: "json",

        success: function (data, textStatus, jqXHR) {
            var text = inputText;
            var spans = data.spans;
            displacyEnt.render(text, spans, ents);
            lastAnalyzedText = text;
            lastNERSpans = spans;
            lastEnts = ents;
        },
        error: function () {
            $('#displacyEntLoader').hide();
            alert('Error while getting NER tags. Please try again.');
        },
        complete: function () {
            $('#displacyEntLoader').hide();
            $('#displacy-ent').show();
        }
    });
    return false;
};

function getPOSAndParse() {
    var inputText = $('#inputText').val();
    displacy.parse(inputText);
};

function visualizeNLPModelOutputs() {
    getNamedEntities();
    getPOSAndParse();
};

function uploadAndClassifyImage() {
    if (imagePredictionsChart != null) {
        imagePredictionsChart.destroy();
    }
    $('#chartLoader').show();
    var files = document.getElementById('resnet50FileUpload').files;
    if (!files.length) {
        $('#chartLoader').hide();
        return alert('Please choose a file to upload first.');
    }
    var file = files[0];
    var fileName = file.name;
    var photoKey = fileName;
    s3.upload({
        Key: photoKey,
        Body: file,
      }, function(err, data) {
        if (err) {
            $('#chartLoader').hide();
            return alert('There was an error uploading your image: ', err.message);
        }
        sendImagePredictionRequestsAndPlotImagePredictionsChart(photoKey);
      });
};

function sendResNetPredictionRequest(photoKey) {
    return $.ajax({
        type: 'GET',
        url: resnet50Endpoint,
        data: {
            imageKey: photoKey
        },
        dataType: 'json',
        error: function() {
            $('#chartLoader').hide();
            alert('There was an error while sending prediction request to ResNet50 model.');
        },
    });
};

function sendInceptionV3PredictionRequest(photoKey) {
    if (inceptionV3Endpoint === '') {
        return false;
    }
    return $.ajax({
        type: 'GET',
        url: inceptionV3Endpoint,
        data: {
            imageKey: photoKey
        },
        dataType: 'json',
        error: function() {
            $('#chartLoader').hide();
            alert('There was an error while sending prediction request to Inception V3 model.');
        },
    });
}

function findIndex(array, element) {
    for (let i=0; i<array.length; i++) {
        if (array[i] == element) {
            return i;
        }
    }
    return -1;
}

function sendImagePredictionRequestsAndPlotImagePredictionsChart(photoKey) {
    $.when(sendResNetPredictionRequest(photoKey), 
        sendInceptionV3PredictionRequest(photoKey)).done(function(resnet50Response, inceptionV3Response) {
        //console.log(resnet50Response);
        //console.log(inceptionV3Response);
        var resnetPredictions = resnet50Response[0]['predictions'];
        var datasets = [];
        var labels = [];
        var resnetDataPoints = [];
        var inceptionDataPoints = [];
        var skippedInceptionLabels = [];
        var skippedInceptionProbs = []; 
        
        for (let i=0; i<resnetPredictions.length; i++) {
            var resnetLabel = resnetPredictions[i]['label'];
            labels.push(resnetLabel);
            resnetDataPoints.push(resnetPredictions[i]['probability']);
            if (inceptionV3Response != false) {
                inceptionLabel = inceptionV3Response[0]['predictions'][i]['label'];
                inceptionProbability = inceptionV3Response[0]['predictions'][i]['probability'];
                if (inceptionLabel == resnetLabel) {
                    inceptionDataPoints.push(inceptionProbability);
                }
                else {
                    inceptionDataPoints.push(0);
                    skippedInceptionLabels.push(inceptionLabel);
                    skippedInceptionProbs.push(inceptionProbability);
                }
            }
        }

        if (inceptionV3Response != false) {
            for (let i=0; i<skippedInceptionProbs.length; i++) {
                inceptionLabel = skippedInceptionLabels[i];
                inceptionProbability = skippedInceptionProbs[i];
                labelIndex = findIndex(labels, inceptionLabel);
                if (labelIndex != -1) {
                    inceptionDataPoints[labelIndex] = inceptionProbability;
                }
                else {
                    labels.push(inceptionLabel);
                    resnetDataPoints.push(0);
                    inceptionDataPoints.push(inceptionProbability);
                }
            }
        }

        //  create datasets...
        resnetBgColor = [];
        resnetBorderColor = [];
        inceptionBgcolor = [];
        inceptionBorderColor = [];
        averagedBgColor = [];
        averagedBorderColor = [];
        for (let i=0; i<labels.length; i++) {
            resnetBgColor.push('rgba(54, 162, 235, 0.2)');
            resnetBorderColor.push('rgba(54, 162, 235, 1)');
            inceptionBgcolor.push('rgba(255, 99, 132, 0.2)');
            inceptionBorderColor.push('rgba(255, 99, 132 ,1)');
            averagedBgColor.push('rgba(153, 102, 255, 0.2)');
            averagedBorderColor.push('rgba(153, 102, 255, 1)');
        }

        var resnetDataset = {
            label: 'ResNet50 probability',
            data: resnetDataPoints,
            backgroundColor: resnetBgColor,
            borderColor: resnetBorderColor,
            borderWidth: 1,
        };
        datasets.push(resnetDataset);

        if (inceptionV3Response != false) {
            var inceptionDataset = {
                label: 'InceptionV3 probability',
                data: inceptionDataPoints,
                backgroundColor: inceptionBgcolor,
                borderColor: inceptionBorderColor,
                borderWidth: 1, 
            };
            datasets.push(inceptionDataset);
            
            // averaging predictions
            averagedDataPoints = [];
            for (let i=0; i<labels.length; i++) {
                point = (resnetDataPoints[i] + inceptionDataPoints[i]) / 2;
                averagedDataPoints.push(point);
            }
            datasets.push({
                label: 'Average probability',
                data: averagedDataPoints,
                backgroundColor: averagedBgColor,
                borderColor: averagedBorderColor,
                borderWidth: 1
            });

        }
        // plot
        plotImagePredictionsChart(labels, datasets);
    });
}

function plotImagePredictionsChart(labels, datasets) {
    $('#chartLoader').hide();
    var ctx = document.getElementById("resnetChart").getContext('2d');
    imagePredictionsChart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: labels,
            datasets: datasets,
        },
        options: {
            title: {
                display: true,
                text: 'ResNet50 vs. InceptionV3 Top 5 Class Probability Predictions'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                    }
                }]
            },
        }
    });
};

function sendHousePredictionRequest() {
    // TODO validate form
    $('#predPriceGroup').hide();
    $('#housingLoader').show();
    $.ajax({
        type: 'GET',
        url: housingEndpoint,
        data: {
            medInc: $('#medInc').val(),
            houseAge: $('#houseAge').val(),
            aveRooms: $('#aveRooms').val(),
            aveBedrms: $('#aveBedrms').val(),
            population: $('#population').val(),
            aveOccup: $('#aveOccup').val(),
            latitude: $('#latitude').val(),
            longitude: $('#longitude').val()
        },
        dataType: 'json',
        error: function(error) {
            alert('Error while obtaining house price prediction. Please check all fields and try again.');
        },
        success: function(data) {
            $('#predPrice').val(data.predictedPrice);
        },
        complete: function() {
            $('#housingLoader').hide();
            $('#predPriceGroup').show();
        }
    });
};

$('#btnAnalyzeText').click(visualizeNLPModelOutputs);
$('#btnPredictHousePrice').click(sendHousePredictionRequest);

$.each(allEntities, function (index, value) {
    var id = '#' + value;
    $(id).click(function () {
        ents = [];
        $.each(allEntities, function (index2, value2) {
            //console.log(index, '#'+value);
            var id2 = '#' + value2;
            if ($(id2).is(':checked')) {
                ents.push(value2);
            }
        });
        displacyEnt.render(lastAnalyzedText, lastNERSpans, ents);
    });
});

$('#select-all').click(function () {
    if ($(this).is(':checked')) {
        $.each(allEntities, function (index, value) {
            var id = '#' + value;
            $(id).prop('checked', true);
        });
        ents = allEntities;
        displacyEnt.render(lastAnalyzedText, lastNERSpans, ents);
    }
    else {
        $.each(allEntities, function (index, value) {
            var id = '#' + value;
            $(id).prop('checked', false);
        });
        ents = [];
        displacyEnt.render(lastAnalyzedText, lastNERSpans, ents);
    }
});

$('#btnResNetUpload').click(uploadAndClassifyImage);

Chart.defaults.global.defaultFontFamily = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif";
Chart.defaults.global.defaultFontSize = 14;
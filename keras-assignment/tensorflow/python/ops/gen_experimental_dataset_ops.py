"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: experimental_dataset_ops.cc
"""

import collections as _collections
import six as _six

from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.eager import execute as _execute
from tensorflow.python.framework import dtypes as _dtypes
from tensorflow.python.framework import errors as _errors
from tensorflow.python.framework import tensor_shape as _tensor_shape

from tensorflow.core.framework import op_def_pb2 as _op_def_pb2
# Needed to trigger the call to _set_call_cpp_shape_fn.
from tensorflow.python.framework import common_shapes as _common_shapes
from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.deprecation import deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export


def experimental_assert_next_dataset(input_dataset, transformations, output_types, output_shapes, name=None):
  r"""TODO: add doc.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    transformations: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_assert_next_dataset' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_assert_next_dataset' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalAssertNextDataset", input_dataset=input_dataset,
        transformations=transformations, output_types=output_types,
        output_shapes=output_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"))
    _execute.record_gradient(
      "ExperimentalAssertNextDataset", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalAssertNextDataset", name, _ctx._post_execution_callbacks,
        input_dataset, transformations, "output_types", output_types,
        "output_shapes", output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_assert_next_dataset_eager_fallback(
          input_dataset, transformations, output_types=output_types,
          output_shapes=output_shapes, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_assert_next_dataset_eager_fallback(input_dataset, transformations, output_types, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_assert_next_dataset
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_assert_next_dataset' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_assert_next_dataset' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  input_dataset = _ops.convert_to_tensor(input_dataset, _dtypes.variant)
  transformations = _ops.convert_to_tensor(transformations, _dtypes.string)
  _inputs_flat = [input_dataset, transformations]
  _attrs = ("output_types", output_types, "output_shapes", output_shapes)
  _result = _execute.execute(b"ExperimentalAssertNextDataset", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalAssertNextDataset", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_csv_dataset(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name=None):
  r"""TODO: add doc.

  Args:
    filenames: A `Tensor` of type `string`.
    compression_type: A `Tensor` of type `string`.
    buffer_size: A `Tensor` of type `int64`.
    header: A `Tensor` of type `bool`.
    field_delim: A `Tensor` of type `string`.
    use_quote_delim: A `Tensor` of type `bool`.
    na_value: A `Tensor` of type `string`.
    select_cols: A `Tensor` of type `int64`.
    record_defaults: A list of `Tensor` objects with types from: `float32`, `float64`, `int32`, `int64`, `string`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_csv_dataset' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalCSVDataset", filenames=filenames,
        compression_type=compression_type, buffer_size=buffer_size,
        header=header, field_delim=field_delim,
        use_quote_delim=use_quote_delim, na_value=na_value,
        select_cols=select_cols, record_defaults=record_defaults,
        output_shapes=output_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"))
    _execute.record_gradient(
      "ExperimentalCSVDataset", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalCSVDataset", name, _ctx._post_execution_callbacks,
        filenames, compression_type, buffer_size, header, field_delim,
        use_quote_delim, na_value, select_cols, record_defaults,
        "output_shapes", output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_csv_dataset_eager_fallback(
          filenames, compression_type, buffer_size, header, field_delim,
          use_quote_delim, na_value, select_cols, record_defaults,
          output_shapes=output_shapes, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_csv_dataset_eager_fallback(filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols, record_defaults, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_csv_dataset
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_csv_dataset' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  _attr_output_types, record_defaults = _execute.convert_to_mixed_eager_tensors(record_defaults, _ctx)
  filenames = _ops.convert_to_tensor(filenames, _dtypes.string)
  compression_type = _ops.convert_to_tensor(compression_type, _dtypes.string)
  buffer_size = _ops.convert_to_tensor(buffer_size, _dtypes.int64)
  header = _ops.convert_to_tensor(header, _dtypes.bool)
  field_delim = _ops.convert_to_tensor(field_delim, _dtypes.string)
  use_quote_delim = _ops.convert_to_tensor(use_quote_delim, _dtypes.bool)
  na_value = _ops.convert_to_tensor(na_value, _dtypes.string)
  select_cols = _ops.convert_to_tensor(select_cols, _dtypes.int64)
  _inputs_flat = [filenames, compression_type, buffer_size, header, field_delim, use_quote_delim, na_value, select_cols] + list(record_defaults)
  _attrs = ("output_types", _attr_output_types, "output_shapes",
  output_shapes)
  _result = _execute.execute(b"ExperimentalCSVDataset", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalCSVDataset", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_directed_interleave_dataset(selector_input_dataset, data_input_datasets, output_types, output_shapes, name=None):
  r"""A substitute for `InterleaveDataset` on a fixed list of `N` datasets.

  Args:
    selector_input_dataset: A `Tensor` of type `variant`.
      A dataset of scalar `DT_INT64` elements that determines which of the
      `N` data inputs should produce the next output element.
    data_input_datasets: A list of at least 1 `Tensor` objects with type `variant`.
      `N` datasets with the same type that will be interleaved according to
      the values of `selector_input_dataset`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(data_input_datasets, (list, tuple)):
      raise TypeError(
          "Expected list for 'data_input_datasets' argument to "
          "'experimental_directed_interleave_dataset' Op, not %r." % data_input_datasets)
    _attr_N = len(data_input_datasets)
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_directed_interleave_dataset' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_directed_interleave_dataset' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalDirectedInterleaveDataset",
        selector_input_dataset=selector_input_dataset,
        data_input_datasets=data_input_datasets, output_types=output_types,
        output_shapes=output_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"), "N", _op.get_attr("N"))
    _execute.record_gradient(
      "ExperimentalDirectedInterleaveDataset", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalDirectedInterleaveDataset", name,
        _ctx._post_execution_callbacks, selector_input_dataset,
        data_input_datasets, "output_types", output_types, "output_shapes",
        output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_directed_interleave_dataset_eager_fallback(
          selector_input_dataset, data_input_datasets,
          output_types=output_types, output_shapes=output_shapes, name=name,
          ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_directed_interleave_dataset_eager_fallback(selector_input_dataset, data_input_datasets, output_types, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_directed_interleave_dataset
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(data_input_datasets, (list, tuple)):
    raise TypeError(
        "Expected list for 'data_input_datasets' argument to "
        "'experimental_directed_interleave_dataset' Op, not %r." % data_input_datasets)
  _attr_N = len(data_input_datasets)
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_directed_interleave_dataset' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_directed_interleave_dataset' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  selector_input_dataset = _ops.convert_to_tensor(selector_input_dataset, _dtypes.variant)
  data_input_datasets = _ops.convert_n_to_tensor(data_input_datasets, _dtypes.variant)
  _inputs_flat = [selector_input_dataset] + list(data_input_datasets)
  _attrs = ("output_types", output_types, "output_shapes", output_shapes, "N",
  _attr_N)
  _result = _execute.execute(b"ExperimentalDirectedInterleaveDataset", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalDirectedInterleaveDataset", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_function_buffering_resource(string_arg, target_device, shared_name, container, f, buffer_size, output_types, name=None):
  r"""Creates a resource that fills up a buffer by making function calls.

  Args:
    string_arg: A `Tensor` of type `string`.
      String argument to the function call.
    target_device: A `Tensor` of type `string`.
      Target device to execute the function on.
    shared_name: A `string`.
      If non-empty, this resource will be shared under the given name across
      multiple sessions.
    container: A `string`.
      If non-empty, this resource is placed in the given container.
      Otherwise, a default container is used.
    f: A function decorated with @Defun. Function to be executed.
    buffer_size: An `int`. Size of the buffer.
    output_types: A list of `tf.DTypes`. The type list for the return values.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    shared_name = _execute.make_str(shared_name, "shared_name")
    container = _execute.make_str(container, "container")
    buffer_size = _execute.make_int(buffer_size, "buffer_size")
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_function_buffering_resource' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalFunctionBufferingResource", string_arg=string_arg,
        target_device=target_device, shared_name=shared_name,
        container=container, f=f, buffer_size=buffer_size,
        output_types=output_types, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("shared_name", _op.get_attr("shared_name"), "container",
              _op.get_attr("container"), "f", _op.get_attr("f"),
              "buffer_size", _op.get_attr("buffer_size"), "output_types",
              _op.get_attr("output_types"))
    _execute.record_gradient(
      "ExperimentalFunctionBufferingResource", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalFunctionBufferingResource", name,
        _ctx._post_execution_callbacks, string_arg, target_device,
        "shared_name", shared_name, "container", container, "f", f,
        "buffer_size", buffer_size, "output_types", output_types)
      return _result
    except _core._FallbackException:
      return experimental_function_buffering_resource_eager_fallback(
          string_arg, target_device, shared_name=shared_name,
          container=container, f=f, buffer_size=buffer_size,
          output_types=output_types, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_function_buffering_resource_eager_fallback(string_arg, target_device, shared_name, container, f, buffer_size, output_types, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_function_buffering_resource
  """
  _ctx = ctx if ctx else _context.context()
  shared_name = _execute.make_str(shared_name, "shared_name")
  container = _execute.make_str(container, "container")
  buffer_size = _execute.make_int(buffer_size, "buffer_size")
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_function_buffering_resource' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  string_arg = _ops.convert_to_tensor(string_arg, _dtypes.string)
  target_device = _ops.convert_to_tensor(target_device, _dtypes.string)
  _inputs_flat = [string_arg, target_device]
  _attrs = ("shared_name", shared_name, "container", container, "f", f,
  "buffer_size", buffer_size, "output_types", output_types)
  _result = _execute.execute(b"ExperimentalFunctionBufferingResource", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalFunctionBufferingResource", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_function_buffering_resource_get_next(function_buffer_resource, output_types, name=None):
  r"""Gets the next element from a FunctionBufferingResource.

  Args:
    function_buffer_resource: A `Tensor` of type `resource`.
      The FunctionBufferingResource handle.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
      The type list for the return values.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_function_buffering_resource_get_next' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalFunctionBufferingResourceGetNext",
        function_buffer_resource=function_buffer_resource,
        output_types=output_types, name=name)
    _result = _op.outputs[:]
    if not _result:
      return _op
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"))
    _execute.record_gradient(
      "ExperimentalFunctionBufferingResourceGetNext", _inputs_flat, _attrs, _result, name)
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalFunctionBufferingResourceGetNext", name,
        _ctx._post_execution_callbacks, function_buffer_resource,
        "output_types", output_types)
      return _result
    except _core._FallbackException:
      return experimental_function_buffering_resource_get_next_eager_fallback(
          function_buffer_resource, output_types=output_types, name=name,
          ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_function_buffering_resource_get_next_eager_fallback(function_buffer_resource, output_types, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_function_buffering_resource_get_next
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_function_buffering_resource_get_next' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  function_buffer_resource = _ops.convert_to_tensor(function_buffer_resource, _dtypes.resource)
  _inputs_flat = [function_buffer_resource]
  _attrs = ("output_types", output_types)
  _result = _execute.execute(b"ExperimentalFunctionBufferingResourceGetNext",
                             len(output_types), inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ExperimentalFunctionBufferingResourceGetNext", _inputs_flat, _attrs, _result, name)
  return _result


def experimental_function_buffering_resource_reset(function_buffer_resource, name=None):
  r"""Resets the FunctionBufferingResource.

  Args:
    function_buffer_resource: A `Tensor` of type `resource`.
      The FunctionBufferingResource handle.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalFunctionBufferingResourceReset",
        function_buffer_resource=function_buffer_resource, name=name)
    return _op
    _result = None
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalFunctionBufferingResourceReset", name,
        _ctx._post_execution_callbacks, function_buffer_resource)
      return _result
    except _core._FallbackException:
      return experimental_function_buffering_resource_reset_eager_fallback(
          function_buffer_resource, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_function_buffering_resource_reset_eager_fallback(function_buffer_resource, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_function_buffering_resource_reset
  """
  _ctx = ctx if ctx else _context.context()
  function_buffer_resource = _ops.convert_to_tensor(function_buffer_resource, _dtypes.resource)
  _inputs_flat = [function_buffer_resource]
  _attrs = None
  _result = _execute.execute(b"ExperimentalFunctionBufferingResourceReset", 0,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _result = None
  return _result


def experimental_identity_indexed_dataset(size, name=None):
  r"""TODO: add doc.

  Args:
    size: A `Tensor` of type `uint64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalIdentityIndexedDataset", size=size, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
    _execute.record_gradient(
      "ExperimentalIdentityIndexedDataset", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalIdentityIndexedDataset", name,
        _ctx._post_execution_callbacks, size)
      return _result
    except _core._FallbackException:
      return experimental_identity_indexed_dataset_eager_fallback(
          size, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_identity_indexed_dataset_eager_fallback(size, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_identity_indexed_dataset
  """
  _ctx = ctx if ctx else _context.context()
  size = _ops.convert_to_tensor(size, _dtypes.uint64)
  _inputs_flat = [size]
  _attrs = None
  _result = _execute.execute(b"ExperimentalIdentityIndexedDataset", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalIdentityIndexedDataset", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_ignore_errors_dataset(input_dataset, output_types, output_shapes, name=None):
  r"""Creates a dataset that contains the elements of `input_dataset` ignoring errors.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_ignore_errors_dataset' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_ignore_errors_dataset' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalIgnoreErrorsDataset", input_dataset=input_dataset,
        output_types=output_types, output_shapes=output_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"))
    _execute.record_gradient(
      "ExperimentalIgnoreErrorsDataset", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalIgnoreErrorsDataset", name,
        _ctx._post_execution_callbacks, input_dataset, "output_types",
        output_types, "output_shapes", output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_ignore_errors_dataset_eager_fallback(
          input_dataset, output_types=output_types,
          output_shapes=output_shapes, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_ignore_errors_dataset_eager_fallback(input_dataset, output_types, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_ignore_errors_dataset
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_ignore_errors_dataset' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_ignore_errors_dataset' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  input_dataset = _ops.convert_to_tensor(input_dataset, _dtypes.variant)
  _inputs_flat = [input_dataset]
  _attrs = ("output_types", output_types, "output_shapes", output_shapes)
  _result = _execute.execute(b"ExperimentalIgnoreErrorsDataset", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalIgnoreErrorsDataset", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_indexed_dataset_get(materialized, index, output_types, output_shapes, name=None):
  r"""TODO: add doc.

  Args:
    materialized: A `Tensor` of type `resource`.
    index: A `Tensor` of type `uint64`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `output_types`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_indexed_dataset_get' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_indexed_dataset_get' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalIndexedDatasetGet", materialized=materialized,
        index=index, output_types=output_types, output_shapes=output_shapes,
        name=name)
    _result = _op.outputs[:]
    if not _result:
      return _op
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"))
    _execute.record_gradient(
      "ExperimentalIndexedDatasetGet", _inputs_flat, _attrs, _result, name)
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalIndexedDatasetGet", name, _ctx._post_execution_callbacks,
        materialized, index, "output_types", output_types, "output_shapes",
        output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_indexed_dataset_get_eager_fallback(
          materialized, index, output_types=output_types,
          output_shapes=output_shapes, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_indexed_dataset_get_eager_fallback(materialized, index, output_types, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_indexed_dataset_get
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_indexed_dataset_get' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_indexed_dataset_get' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  materialized = _ops.convert_to_tensor(materialized, _dtypes.resource)
  index = _ops.convert_to_tensor(index, _dtypes.uint64)
  _inputs_flat = [materialized, index]
  _attrs = ("output_types", output_types, "output_shapes", output_shapes)
  _result = _execute.execute(b"ExperimentalIndexedDatasetGet",
                             len(output_types), inputs=_inputs_flat,
                             attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ExperimentalIndexedDatasetGet", _inputs_flat, _attrs, _result, name)
  return _result


def experimental_indexed_dataset_materialize(dataset, materialized, name=None):
  r"""TODO: add doc.

  Args:
    dataset: A `Tensor` of type `variant`.
    materialized: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalIndexedDatasetMaterialize", dataset=dataset,
        materialized=materialized, name=name)
    return _op
    _result = None
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalIndexedDatasetMaterialize", name,
        _ctx._post_execution_callbacks, dataset, materialized)
      return _result
    except _core._FallbackException:
      return experimental_indexed_dataset_materialize_eager_fallback(
          dataset, materialized, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_indexed_dataset_materialize_eager_fallback(dataset, materialized, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_indexed_dataset_materialize
  """
  _ctx = ctx if ctx else _context.context()
  dataset = _ops.convert_to_tensor(dataset, _dtypes.variant)
  materialized = _ops.convert_to_tensor(materialized, _dtypes.resource)
  _inputs_flat = [dataset, materialized]
  _attrs = None
  _result = _execute.execute(b"ExperimentalIndexedDatasetMaterialize", 0,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _result = None
  return _result


def experimental_iterator_get_device(resource, name=None):
  r"""Returns the name of the device on which `resource` has been placed.

  Args:
    resource: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalIteratorGetDevice", resource=resource, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
    _execute.record_gradient(
      "ExperimentalIteratorGetDevice", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalIteratorGetDevice", name, _ctx._post_execution_callbacks,
        resource)
      return _result
    except _core._FallbackException:
      return experimental_iterator_get_device_eager_fallback(
          resource, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_iterator_get_device_eager_fallback(resource, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_iterator_get_device
  """
  _ctx = ctx if ctx else _context.context()
  resource = _ops.convert_to_tensor(resource, _dtypes.resource)
  _inputs_flat = [resource]
  _attrs = None
  _result = _execute.execute(b"ExperimentalIteratorGetDevice", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalIteratorGetDevice", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_lmdb_dataset(filenames, output_types, output_shapes, name=None):
  r"""TODO: add doc.

  Args:
    filenames: A `Tensor` of type `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_lmdb_dataset' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_lmdb_dataset' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalLMDBDataset", filenames=filenames,
        output_types=output_types, output_shapes=output_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"))
    _execute.record_gradient(
      "ExperimentalLMDBDataset", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalLMDBDataset", name, _ctx._post_execution_callbacks,
        filenames, "output_types", output_types, "output_shapes",
        output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_lmdb_dataset_eager_fallback(
          filenames, output_types=output_types, output_shapes=output_shapes,
          name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_lmdb_dataset_eager_fallback(filenames, output_types, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_lmdb_dataset
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_lmdb_dataset' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_lmdb_dataset' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  filenames = _ops.convert_to_tensor(filenames, _dtypes.string)
  _inputs_flat = [filenames]
  _attrs = ("output_types", output_types, "output_shapes", output_shapes)
  _result = _execute.execute(b"ExperimentalLMDBDataset", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalLMDBDataset", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_materialized_index_dataset_handle(container, shared_name, output_types, output_shapes, name=None):
  r"""TODO: add doc.

  Args:
    container: A `string`.
    shared_name: A `string`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    container = _execute.make_str(container, "container")
    shared_name = _execute.make_str(shared_name, "shared_name")
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_materialized_index_dataset_handle' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_materialized_index_dataset_handle' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalMaterializedIndexDatasetHandle", container=container,
        shared_name=shared_name, output_types=output_types,
        output_shapes=output_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("container", _op.get_attr("container"), "shared_name",
              _op.get_attr("shared_name"), "output_types",
              _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"))
    _execute.record_gradient(
      "ExperimentalMaterializedIndexDatasetHandle", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalMaterializedIndexDatasetHandle", name,
        _ctx._post_execution_callbacks, "container", container, "shared_name",
        shared_name, "output_types", output_types, "output_shapes",
        output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_materialized_index_dataset_handle_eager_fallback(
          container=container, shared_name=shared_name,
          output_types=output_types, output_shapes=output_shapes, name=name,
          ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_materialized_index_dataset_handle_eager_fallback(container, shared_name, output_types, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_materialized_index_dataset_handle
  """
  _ctx = ctx if ctx else _context.context()
  container = _execute.make_str(container, "container")
  shared_name = _execute.make_str(shared_name, "shared_name")
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_materialized_index_dataset_handle' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_materialized_index_dataset_handle' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  _inputs_flat = []
  _attrs = ("container", container, "shared_name", shared_name,
  "output_types", output_types, "output_shapes", output_shapes)
  _result = _execute.execute(b"ExperimentalMaterializedIndexDatasetHandle", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalMaterializedIndexDatasetHandle", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_thread_pool_dataset(input_dataset, thread_pool, output_types, output_shapes, name=None):
  r"""Creates a dataset that uses a custom thread pool to compute `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    thread_pool: A `Tensor` of type `resource`.
      A resource produced by the ThreadPoolHandle op.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_thread_pool_dataset' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_thread_pool_dataset' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalThreadPoolDataset", input_dataset=input_dataset,
        thread_pool=thread_pool, output_types=output_types,
        output_shapes=output_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"))
    _execute.record_gradient(
      "ExperimentalThreadPoolDataset", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalThreadPoolDataset", name, _ctx._post_execution_callbacks,
        input_dataset, thread_pool, "output_types", output_types,
        "output_shapes", output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_thread_pool_dataset_eager_fallback(
          input_dataset, thread_pool, output_types=output_types,
          output_shapes=output_shapes, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_thread_pool_dataset_eager_fallback(input_dataset, thread_pool, output_types, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_thread_pool_dataset
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_thread_pool_dataset' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_thread_pool_dataset' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  input_dataset = _ops.convert_to_tensor(input_dataset, _dtypes.variant)
  thread_pool = _ops.convert_to_tensor(thread_pool, _dtypes.resource)
  _inputs_flat = [input_dataset, thread_pool]
  _attrs = ("output_types", output_types, "output_shapes", output_shapes)
  _result = _execute.execute(b"ExperimentalThreadPoolDataset", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalThreadPoolDataset", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_thread_pool_handle(num_threads, display_name, max_intra_op_parallelism=1, container="", shared_name="", name=None):
  r"""Creates a dataset that uses a custom thread pool to compute `input_dataset`.

  Args:
    num_threads: An `int`. The number of threads in the thread pool.
    display_name: A `string`.
      A human-readable name for the threads that may be visible in some
      visualizations.
      threadpool.
    max_intra_op_parallelism: An optional `int`. Defaults to `1`.
      The maximum degree of parallelism to use within operations that execute on this
      threadpool.
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    num_threads = _execute.make_int(num_threads, "num_threads")
    display_name = _execute.make_str(display_name, "display_name")
    if max_intra_op_parallelism is None:
      max_intra_op_parallelism = 1
    max_intra_op_parallelism = _execute.make_int(max_intra_op_parallelism, "max_intra_op_parallelism")
    if container is None:
      container = ""
    container = _execute.make_str(container, "container")
    if shared_name is None:
      shared_name = ""
    shared_name = _execute.make_str(shared_name, "shared_name")
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalThreadPoolHandle", num_threads=num_threads,
        display_name=display_name,
        max_intra_op_parallelism=max_intra_op_parallelism,
        container=container, shared_name=shared_name, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("num_threads", _op.get_attr("num_threads"),
              "max_intra_op_parallelism",
              _op.get_attr("max_intra_op_parallelism"), "display_name",
              _op.get_attr("display_name"), "container",
              _op.get_attr("container"), "shared_name",
              _op.get_attr("shared_name"))
    _execute.record_gradient(
      "ExperimentalThreadPoolHandle", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalThreadPoolHandle", name, _ctx._post_execution_callbacks,
        "num_threads", num_threads, "max_intra_op_parallelism",
        max_intra_op_parallelism, "display_name", display_name, "container",
        container, "shared_name", shared_name)
      return _result
    except _core._FallbackException:
      return experimental_thread_pool_handle_eager_fallback(
          num_threads=num_threads,
          max_intra_op_parallelism=max_intra_op_parallelism,
          display_name=display_name, container=container,
          shared_name=shared_name, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_thread_pool_handle_eager_fallback(num_threads, display_name, max_intra_op_parallelism=1, container="", shared_name="", name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_thread_pool_handle
  """
  _ctx = ctx if ctx else _context.context()
  num_threads = _execute.make_int(num_threads, "num_threads")
  display_name = _execute.make_str(display_name, "display_name")
  if max_intra_op_parallelism is None:
    max_intra_op_parallelism = 1
  max_intra_op_parallelism = _execute.make_int(max_intra_op_parallelism, "max_intra_op_parallelism")
  if container is None:
    container = ""
  container = _execute.make_str(container, "container")
  if shared_name is None:
    shared_name = ""
  shared_name = _execute.make_str(shared_name, "shared_name")
  _inputs_flat = []
  _attrs = ("num_threads", num_threads, "max_intra_op_parallelism",
  max_intra_op_parallelism, "display_name", display_name, "container",
  container, "shared_name", shared_name)
  _result = _execute.execute(b"ExperimentalThreadPoolHandle", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalThreadPoolHandle", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def experimental_unique_dataset(input_dataset, output_types, output_shapes, name=None):
  r"""Creates a dataset that contains the unique elements of `input_dataset`.

  Args:
    input_dataset: A `Tensor` of type `variant`.
    output_types: A list of `tf.DTypes` that has length `>= 1`.
    output_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`) that has length `>= 1`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `variant`.
  """
  _ctx = _context._context
  if _ctx is None or not _ctx._eager_context.is_eager:
    if not isinstance(output_types, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_types' argument to "
          "'experimental_unique_dataset' Op, not %r." % output_types)
    output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
    if not isinstance(output_shapes, (list, tuple)):
      raise TypeError(
          "Expected list for 'output_shapes' argument to "
          "'experimental_unique_dataset' Op, not %r." % output_shapes)
    output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
    _, _, _op = _op_def_lib._apply_op_helper(
        "ExperimentalUniqueDataset", input_dataset=input_dataset,
        output_types=output_types, output_shapes=output_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("output_types", _op.get_attr("output_types"), "output_shapes",
              _op.get_attr("output_shapes"))
    _execute.record_gradient(
      "ExperimentalUniqueDataset", _inputs_flat, _attrs, _result, name)
    _result, = _result
    return _result

  else:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, _ctx._eager_context.device_name,
        "ExperimentalUniqueDataset", name, _ctx._post_execution_callbacks,
        input_dataset, "output_types", output_types, "output_shapes",
        output_shapes)
      return _result
    except _core._FallbackException:
      return experimental_unique_dataset_eager_fallback(
          input_dataset, output_types=output_types,
          output_shapes=output_shapes, name=name, ctx=_ctx)
    except _core._NotOkStatusException as e:
      if name is not None:
        message = e.message + " name: " + name
      else:
        message = e.message
      _six.raise_from(_core._status_to_exception(e.code, message), None)


def experimental_unique_dataset_eager_fallback(input_dataset, output_types, output_shapes, name=None, ctx=None):
  r"""This is the slowpath function for Eager mode.
  This is for function experimental_unique_dataset
  """
  _ctx = ctx if ctx else _context.context()
  if not isinstance(output_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_types' argument to "
        "'experimental_unique_dataset' Op, not %r." % output_types)
  output_types = [_execute.make_type(_t, "output_types") for _t in output_types]
  if not isinstance(output_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'output_shapes' argument to "
        "'experimental_unique_dataset' Op, not %r." % output_shapes)
  output_shapes = [_execute.make_shape(_s, "output_shapes") for _s in output_shapes]
  input_dataset = _ops.convert_to_tensor(input_dataset, _dtypes.variant)
  _inputs_flat = [input_dataset]
  _attrs = ("output_types", output_types, "output_shapes", output_shapes)
  _result = _execute.execute(b"ExperimentalUniqueDataset", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                             name=name)
  _execute.record_gradient(
      "ExperimentalUniqueDataset", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "ExperimentalAssertNextDataset"
#   input_arg {
#     name: "input_dataset"
#     type: DT_VARIANT
#   }
#   input_arg {
#     name: "transformations"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "handle"
#     type: DT_VARIANT
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
# }
# op {
#   name: "ExperimentalCSVDataset"
#   input_arg {
#     name: "filenames"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "compression_type"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "buffer_size"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "header"
#     type: DT_BOOL
#   }
#   input_arg {
#     name: "field_delim"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "use_quote_delim"
#     type: DT_BOOL
#   }
#   input_arg {
#     name: "na_value"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "select_cols"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "record_defaults"
#     type_list_attr: "output_types"
#   }
#   output_arg {
#     name: "handle"
#     type: DT_VARIANT
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT32
#         type: DT_INT64
#         type: DT_STRING
#       }
#     }
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalDirectedInterleaveDataset"
#   input_arg {
#     name: "selector_input_dataset"
#     type: DT_VARIANT
#   }
#   input_arg {
#     name: "data_input_datasets"
#     type: DT_VARIANT
#     number_attr: "N"
#   }
#   output_arg {
#     name: "handle"
#     type: DT_VARIANT
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "N"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
# }
# op {
#   name: "ExperimentalFunctionBufferingResource"
#   input_arg {
#     name: "string_arg"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "target_device"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "resource"
#     type: DT_RESOURCE
#   }
#   attr {
#     name: "shared_name"
#     type: "string"
#   }
#   attr {
#     name: "container"
#     type: "string"
#   }
#   attr {
#     name: "f"
#     type: "func"
#   }
#   attr {
#     name: "buffer_size"
#     type: "int"
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalFunctionBufferingResourceGetNext"
#   input_arg {
#     name: "function_buffer_resource"
#     type: DT_RESOURCE
#   }
#   output_arg {
#     name: "output"
#     type_list_attr: "output_types"
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalFunctionBufferingResourceReset"
#   input_arg {
#     name: "function_buffer_resource"
#     type: DT_RESOURCE
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalIdentityIndexedDataset"
#   input_arg {
#     name: "size"
#     type: DT_UINT64
#   }
#   output_arg {
#     name: "handle"
#     type: DT_VARIANT
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalIgnoreErrorsDataset"
#   input_arg {
#     name: "input_dataset"
#     type: DT_VARIANT
#   }
#   output_arg {
#     name: "handle"
#     type: DT_VARIANT
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
# }
# op {
#   name: "ExperimentalIndexedDatasetGet"
#   input_arg {
#     name: "materialized"
#     type: DT_RESOURCE
#   }
#   input_arg {
#     name: "index"
#     type: DT_UINT64
#   }
#   output_arg {
#     name: "components"
#     type_list_attr: "output_types"
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalIndexedDatasetMaterialize"
#   input_arg {
#     name: "dataset"
#     type: DT_VARIANT
#   }
#   input_arg {
#     name: "materialized"
#     type: DT_RESOURCE
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalIteratorGetDevice"
#   input_arg {
#     name: "resource"
#     type: DT_RESOURCE
#   }
#   output_arg {
#     name: "device"
#     type: DT_STRING
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalLMDBDataset"
#   input_arg {
#     name: "filenames"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "handle"
#     type: DT_VARIANT
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalMaterializedIndexDatasetHandle"
#   output_arg {
#     name: "handle"
#     type: DT_RESOURCE
#   }
#   attr {
#     name: "container"
#     type: "string"
#   }
#   attr {
#     name: "shared_name"
#     type: "string"
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalThreadPoolDataset"
#   input_arg {
#     name: "input_dataset"
#     type: DT_VARIANT
#   }
#   input_arg {
#     name: "thread_pool"
#     type: DT_RESOURCE
#   }
#   output_arg {
#     name: "handle"
#     type: DT_VARIANT
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalThreadPoolHandle"
#   output_arg {
#     name: "handle"
#     type: DT_RESOURCE
#   }
#   attr {
#     name: "num_threads"
#     type: "int"
#   }
#   attr {
#     name: "max_intra_op_parallelism"
#     type: "int"
#     default_value {
#       i: 1
#     }
#   }
#   attr {
#     name: "display_name"
#     type: "string"
#   }
#   attr {
#     name: "container"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   attr {
#     name: "shared_name"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "ExperimentalUniqueDataset"
#   input_arg {
#     name: "input_dataset"
#     type: DT_VARIANT
#   }
#   output_arg {
#     name: "handle"
#     type: DT_VARIANT
#   }
#   attr {
#     name: "output_types"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "output_shapes"
#     type: "list(shape)"
#     has_minimum: true
#     minimum: 1
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n\225\001\n\035ExperimentalAssertNextDataset\022\021\n\rinput_dataset\030\025\022\023\n\017transformations\030\007\032\n\n\006handle\030\025\"\036\n\014output_types\022\nlist(type)(\0010\001\" \n\routput_shapes\022\013list(shape)(\0010\001\n\234\002\n\026ExperimentalCSVDataset\022\r\n\tfilenames\030\007\022\024\n\020compression_type\030\007\022\017\n\013buffer_size\030\t\022\n\n\006header\030\n\022\017\n\013field_delim\030\007\022\023\n\017use_quote_delim\030\n\022\014\n\010na_value\030\007\022\017\n\013select_cols\030\t\022\037\n\017record_defaults2\014output_types\032\n\n\006handle\030\025\")\n\014output_types\022\nlist(type)(\0010\001:\t\n\0072\005\001\002\003\t\007\" \n\routput_shapes\022\013list(shape)(\0010\001\210\001\001\n\273\001\n%ExperimentalDirectedInterleaveDataset\022\032\n\026selector_input_dataset\030\025\022\032\n\023data_input_datasets\030\025*\001N\032\n\n\006handle\030\025\"\036\n\014output_types\022\nlist(type)(\0010\001\" \n\routput_shapes\022\013list(shape)(\0010\001\"\014\n\001N\022\003int(\0010\001\n\302\001\n%ExperimentalFunctionBufferingResource\022\016\n\nstring_arg\030\007\022\021\n\rtarget_device\030\007\032\014\n\010resource\030\024\"\025\n\013shared_name\022\006string\"\023\n\tcontainer\022\006string\"\t\n\001f\022\004func\"\022\n\013buffer_size\022\003int\"\032\n\014output_types\022\nlist(type)\210\001\001\n\207\001\n,ExperimentalFunctionBufferingResourceGetNext\022\034\n\030function_buffer_resource\030\024\032\026\n\006output2\014output_types\"\036\n\014output_types\022\nlist(type)(\0010\001\210\001\001\nM\n*ExperimentalFunctionBufferingResourceReset\022\034\n\030function_buffer_resource\030\024\210\001\001\n=\n\"ExperimentalIdentityIndexedDataset\022\010\n\004size\030\027\032\n\n\006handle\030\025\210\001\001\n\202\001\n\037ExperimentalIgnoreErrorsDataset\022\021\n\rinput_dataset\030\025\032\n\n\006handle\030\025\"\036\n\014output_types\022\nlist(type)(\0010\001\" \n\routput_shapes\022\013list(shape)(\0010\001\n\235\001\n\035ExperimentalIndexedDatasetGet\022\020\n\014materialized\030\024\022\t\n\005index\030\027\032\032\n\ncomponents2\014output_types\"\036\n\014output_types\022\nlist(type)(\0010\001\" \n\routput_shapes\022\013list(shape)(\0010\001\210\001\001\nI\n%ExperimentalIndexedDatasetMaterialize\022\013\n\007dataset\030\025\022\020\n\014materialized\030\024\210\001\001\n<\n\035ExperimentalIteratorGetDevice\022\014\n\010resource\030\024\032\n\n\006device\030\007\210\001\001\ny\n\027ExperimentalLMDBDataset\022\r\n\tfilenames\030\007\032\n\n\006handle\030\025\"\036\n\014output_types\022\nlist(type)(\0010\001\" \n\routput_shapes\022\013list(shape)(\0010\001\210\001\001\n\251\001\n*ExperimentalMaterializedIndexDatasetHandle\032\n\n\006handle\030\024\"\023\n\tcontainer\022\006string\"\025\n\013shared_name\022\006string\"\036\n\014output_types\022\nlist(type)(\0010\001\" \n\routput_shapes\022\013list(shape)(\0010\001\210\001\001\n\224\001\n\035ExperimentalThreadPoolDataset\022\021\n\rinput_dataset\030\025\022\017\n\013thread_pool\030\024\032\n\n\006handle\030\025\"\036\n\014output_types\022\nlist(type)(\0010\001\" \n\routput_shapes\022\013list(shape)(\0010\001\210\001\001\n\262\001\n\034ExperimentalThreadPoolHandle\032\n\n\006handle\030\024\"\022\n\013num_threads\022\003int\"#\n\030max_intra_op_parallelism\022\003int\032\002\030\001\"\026\n\014display_name\022\006string\"\027\n\tcontainer\022\006string\032\002\022\000\"\031\n\013shared_name\022\006string\032\002\022\000\210\001\001\n|\n\031ExperimentalUniqueDataset\022\021\n\rinput_dataset\030\025\032\n\n\006handle\030\025\"\036\n\014output_types\022\nlist(type)(\0010\001\" \n\routput_shapes\022\013list(shape)(\0010\001")

// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from custom_interfaces:msg/TargetCor.idl
// generated code does not contain a copyright notice
#include "custom_interfaces/msg/detail/target_cor__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `uyari`
#include "rosidl_runtime_c/string_functions.h"

bool
custom_interfaces__msg__TargetCor__init(custom_interfaces__msg__TargetCor * msg)
{
  if (!msg) {
    return false;
  }
  // uyari
  if (!rosidl_runtime_c__String__init(&msg->uyari)) {
    custom_interfaces__msg__TargetCor__fini(msg);
    return false;
  }
  return true;
}

void
custom_interfaces__msg__TargetCor__fini(custom_interfaces__msg__TargetCor * msg)
{
  if (!msg) {
    return;
  }
  // uyari
  rosidl_runtime_c__String__fini(&msg->uyari);
}

bool
custom_interfaces__msg__TargetCor__are_equal(const custom_interfaces__msg__TargetCor * lhs, const custom_interfaces__msg__TargetCor * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // uyari
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->uyari), &(rhs->uyari)))
  {
    return false;
  }
  return true;
}

bool
custom_interfaces__msg__TargetCor__copy(
  const custom_interfaces__msg__TargetCor * input,
  custom_interfaces__msg__TargetCor * output)
{
  if (!input || !output) {
    return false;
  }
  // uyari
  if (!rosidl_runtime_c__String__copy(
      &(input->uyari), &(output->uyari)))
  {
    return false;
  }
  return true;
}

custom_interfaces__msg__TargetCor *
custom_interfaces__msg__TargetCor__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__msg__TargetCor * msg = (custom_interfaces__msg__TargetCor *)allocator.allocate(sizeof(custom_interfaces__msg__TargetCor), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(custom_interfaces__msg__TargetCor));
  bool success = custom_interfaces__msg__TargetCor__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
custom_interfaces__msg__TargetCor__destroy(custom_interfaces__msg__TargetCor * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    custom_interfaces__msg__TargetCor__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
custom_interfaces__msg__TargetCor__Sequence__init(custom_interfaces__msg__TargetCor__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__msg__TargetCor * data = NULL;

  if (size) {
    data = (custom_interfaces__msg__TargetCor *)allocator.zero_allocate(size, sizeof(custom_interfaces__msg__TargetCor), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = custom_interfaces__msg__TargetCor__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        custom_interfaces__msg__TargetCor__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
custom_interfaces__msg__TargetCor__Sequence__fini(custom_interfaces__msg__TargetCor__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      custom_interfaces__msg__TargetCor__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

custom_interfaces__msg__TargetCor__Sequence *
custom_interfaces__msg__TargetCor__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  custom_interfaces__msg__TargetCor__Sequence * array = (custom_interfaces__msg__TargetCor__Sequence *)allocator.allocate(sizeof(custom_interfaces__msg__TargetCor__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = custom_interfaces__msg__TargetCor__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
custom_interfaces__msg__TargetCor__Sequence__destroy(custom_interfaces__msg__TargetCor__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    custom_interfaces__msg__TargetCor__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
custom_interfaces__msg__TargetCor__Sequence__are_equal(const custom_interfaces__msg__TargetCor__Sequence * lhs, const custom_interfaces__msg__TargetCor__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!custom_interfaces__msg__TargetCor__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
custom_interfaces__msg__TargetCor__Sequence__copy(
  const custom_interfaces__msg__TargetCor__Sequence * input,
  custom_interfaces__msg__TargetCor__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(custom_interfaces__msg__TargetCor);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    custom_interfaces__msg__TargetCor * data =
      (custom_interfaces__msg__TargetCor *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!custom_interfaces__msg__TargetCor__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          custom_interfaces__msg__TargetCor__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!custom_interfaces__msg__TargetCor__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

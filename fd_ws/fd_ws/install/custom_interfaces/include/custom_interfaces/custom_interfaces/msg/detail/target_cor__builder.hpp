// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:msg/TargetCor.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__TARGET_COR__BUILDER_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__TARGET_COR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/msg/detail/target_cor__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace msg
{

namespace builder
{

class Init_TargetCor_uyari
{
public:
  Init_TargetCor_uyari()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::msg::TargetCor uyari(::custom_interfaces::msg::TargetCor::_uyari_type arg)
  {
    msg_.uyari = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::TargetCor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::msg::TargetCor>()
{
  return custom_interfaces::msg::builder::Init_TargetCor_uyari();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__TARGET_COR__BUILDER_HPP_

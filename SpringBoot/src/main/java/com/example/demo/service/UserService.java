package com.example.demo.service;

import com.example.demo.entity.UserEntity;
import java.util.List;

public interface UserService {
UserEntity createUser(UserEntity user);
UserEntity getUserById(Long id);
List<UserEntity> getAllUsers();
UserEntity updateUser(Long id, UserEntity user);
void deleteUser(Long id);
}
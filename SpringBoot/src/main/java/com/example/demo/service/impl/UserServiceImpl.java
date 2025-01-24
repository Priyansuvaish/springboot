package com.example.demo.service.impl;

import com.example.demo.entity.UserEntity;
import com.example.demo.repository.UserRepository;
import com.example.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserServiceImpl implements UserService {

@Autowired
private UserRepository userRepository;

@Override
public UserEntity createUser(UserEntity user) {
return userRepository.save(user);
}

@Override
public UserEntity getUserById(Long id) {
Optional<UserEntity> user = userRepository.findById(id);
return user.orElse(null);
}

@Override
public List<UserEntity> getAllUsers() {
return userRepository.findAll();
}

    @Override
    public UserEntity updateUser(Long id, UserEntity user) {
        return null;
    }

    @Override
public void deleteUser(Long id) {
userRepository.deleteById(id);
}
}
package com.example.demo.controller;

import com.example.demo.entity.UserEntity;
import com.example.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {

@Autowired
private UserService userService;

@PostMapping
public ResponseEntity<UserEntity> createUser(@RequestBody UserEntity user) {
return ResponseEntity.ok(userService.createUser(user));
}

@GetMapping("/{id}")
public ResponseEntity<UserEntity> getUserById(@PathVariable Long id) {
return ResponseEntity.ok(userService.getUserById(id));
}

@GetMapping
public ResponseEntity<List<UserEntity>> getAllUsers() {
return ResponseEntity.ok(userService.getAllUsers());
}

@PutMapping("/{id}")
public ResponseEntity<UserEntity> updateUser(@PathVariable Long id, @RequestBody UserEntity user) {
return ResponseEntity.ok(userService.updateUser(id, user));
}

@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
userService.deleteUser(id);
return ResponseEntity.noContent().build();
}
}
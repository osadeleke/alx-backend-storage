-- SQL script that creates a table users

-- create database if does not exist
CREATE DATABASE IF NOT EXISTS holberton;

-- create table
CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255)
);

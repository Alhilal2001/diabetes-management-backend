CREATE DATABASE diabetesmanagement;

CREATE USER diabetes_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE diabetesmanagement TO diabetes_admin;

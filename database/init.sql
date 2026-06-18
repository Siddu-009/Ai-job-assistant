CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    user_id INT,
    filename VARCHAR(255)
);

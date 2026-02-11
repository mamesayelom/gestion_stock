CREATE TABLE utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'user') DEFAULT 'user'
);

INSERT INTO utilisateurs(prenom, nom, email, password, role) VALUES
("Aliou", "DIALLO", "aliou@gmail.com", "Passer@123", "admin"),
("Mame Saye", "LOM", "mamesaye@gmail.com", "User@123", "user");
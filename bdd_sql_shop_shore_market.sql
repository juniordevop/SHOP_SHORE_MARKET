
CREATE DATABASE projet_boutique;
USE projet_boutique;
CREATE TABLE projet_boutique.Articles (
    Code_p INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(255) NOT NULL,
    Marque VARCHAR(255),
    prix INT NOT NULL,
    stock INT
) AUTO_INCREMENT = 1;
-- Insérer des articles dans la table "Articles" (suppose que les colonnes sont dans l'ordre : Code_p, Type, Marque, prix, stock)

CREATE TABLE projet_boutique.Articles_par_boutique (
    Code_p INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(255) NOT NULL,
    Marque VARCHAR(255),
    prix INT NOT NULL,
    stock INT bank_group
) AUTO_INCREMENT = 1;

CREATE TABLE projet_boutique.boutique(
    Code_B INT AUTO_INCREMENT PRIMARY KEY,
    Nom VARCHAR (255)
) AUTO_INCREMENT = 1;
-- Insérer des articles dans la table "Articles" (suppose que les colonnes sont dans l'ordre : Code_p, Type, Marque, prix, stock)

INSERT INTO projet_boutique.boutique (Nom) VALUES
    ('Chic Mode'),
    ('Diop Technologie'),
    ('Mon Electromenagé');

CREATE TABLE projet_boutique.Diop_Technologie (
    Code_p INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(255) NOT NULL,
    Marque VARCHAR(255),
    prix INT NOT NULL,
    stock INT
) AUTO_INCREMENT = 1;
-- Insérer des articles dans la table "Articles" (suppose que les colonnes sont dans l'ordre : Code_p, Type, Marque, prix, stock)

CREATE TABLE projet_boutique.Mon_Electromenage (
    Code_p INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(255) NOT NULL,
    Marque VARCHAR(255),
    prix INT NOT NULL,
    stock INT
) AUTO_INCREMENT = 1;
-- Insérer des articles dans la table "Articles" (suppose que les colonnes sont dans l'ordre : Code_p, Type, Marque, prix, stock)

CREATE TABLE projet_boutique.Chic_Mode(
    Code_p INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(255) NOT NULL,
    Marque VARCHAR(255),
    prix INT NOT NULL,
    stock INT
) AUTO_INCREMENT = 1;
-- Insérer des articles dans la table "Articles" (suppose que les colonnes sont dans l'ordre : Code_p, Type, Marque, prix, stock)

INSERT INTO projet_boutique.Articles (Type, Marque, prix, stock) VALUES
    ('Chemise', 'Hugo Boss', 59.99, 100),
    ('Jeans', 'Levi Strauss', 69.99, 80),
    ('T-shirt', 'Nike', 29.99, 120),
    ('Costume', 'Calvin Klein', 199.99, 50),
    ('Polo', 'Lacoste', 49.99, 70),
    ('Veste', 'The North Face', 119.99, 60),
    ('Pull', 'Tommy Hilfiger', 79.99, 90),
    ('Shorts', 'Adidas', 39.99, 110),
    ('Blazer', 'Ralph Lauren', 149.99, 40),
    ('Sweat à capuche', 'Puma', 54.99, 75),
    ('Chaussures de sport', 'New Balance', 89.99, 65),
    ('Blouson en cuir', 'Guess', 179.99, 30),
    ('Chino', 'Dockers', 49.99, 85),
    ('Manteau', 'Burberry', 249.99, 25),
    ('Casquette', 'Under Armour', 19.99, 150);
	
INSERT INTO projet_boutique.chic_mode (Type, Marque, prix, stock) VALUES
    ('Chemise', 'Hugo Boss', 35000, 100),
    ('Jeans', 'Levi Strauss', 43000, 80),
    ('T-shirt', 'Nike', 15000, 120),
    ('Costume', 'Calvin Klein', 90000, 50),
    ('Polo', 'Lacoste', 25000, 70),
    ('Veste', 'The North Face', 60000, 60),
    ('Pull', 'Tommy Hilfiger', 55000, 90),
    ('Shorts', 'Adidas', 22000, 110),
    ('Blazer', 'Ralph Lauren', 70000, 40),
    ('Sweat à capuche', 'Puma', 2500, 75),
    ('Chaussures de sport', 'New Balance', 45000, 65),
    ('Blouson en cuir', 'Guess', 130000, 30),
    ('Chino', 'Dockers', 35000, 85),
    ('Manteau', 'Burberry', 170000, 25),
    ('Casquette', 'Under Armour', 80000, 150);


INSERT INTO projet_boutique.diop_technologie (Type, Marque, prix, stock) VALUES
    ('Smartphone', 'Samsung Galaxy S21', 250000, 50),
    ('Smartphone', 'iPhone 13', 300000, 40),
    ('Smartphone', 'Google Pixel 6', 275000, 30),
    ('Smartphone', 'OnePlus 9', 240000, 45),
    ('Smartphone', 'Xiaomi Mi 11', 190000, 55),
    ('Smartphone', 'Sony Xperia 1 III', 250000, 35),
    ('Smartphone', 'Huawei P40 Pro', 230000, 48),
    ('Smartphone', 'Oppo Find X3 Pro', 270000, 38),
    ('Smartphone', 'Asus ROG Phone 5', 280000, 33),
    ('Smartphone', 'Motorola Edge 20', 2000000, 60),
    ('Smartphone', 'Realme GT', 175000, 65),
    ('Smartphone', 'Vivo X60 Pro', 220000, 53),
    ('Smartphone', 'Nokia 9 PureView', 170000, 70),
    ('Smartphone', 'LG G8 ThinQ', 150000, 75),
    ('Smartphone', 'BlackBerry KEY2', 140000, 80);

INSERT INTO projet_boutique.Electromenage (Type, Marque, prix, stock) VALUES
    ('Réfrigérateur', 'Samsung', 349999, 30),
    ('Machine à laver', 'LG', 279999, 40),
    ('Cuisinière', 'Bosch', 239999, 25),
    ('Lave-vaisselle', 'Whirlpool', 319999, 20),
    ('Micro-ondes', 'Panasonic', 79999, 60),
    ('Aspirateur', 'Dyson', 199999, 35),
    ('Mixeur', 'KitchenAid', 89999, 50),
    ('Fer à repasser', 'Rowenta', 59999, 55),
    ('Cafetière', 'Nespresso', 149999, 45),
    ('Grille-pain', 'Philips', 49999, 70),
    ('Four électrique', 'Siemens', 269999, 30),
    ('Robot culinaire', 'Kenwood', 179999, 40),
    ('Centrale vapeur', 'Tefal', 219999, 35),
    ('Hachoir', 'Moulinex', 69999, 60),
    ('Bouilloire électrique', 'Russell Hobbs', 39999, 75);



Create table projet_boutique.BANK_GROUP(
    num_compte INT AUTO_INCREMENT PRIMARY KEY,
    Type_compte VARCHAR(255) NOT NULL,
    prenom VARCHAR(255),
    nom VARCHAR(255),
    mdp INT NOT NULL,
    solde INT
) AUTO_INCREMENT = 001;

-- Insérer des clients dans la table "BANK_GROUP" (suppose que les colonnes sont dans l'ordre : num_compte, Type_compte, prenom, nom, mdp, solde)

-- Boutiques
INSERT INTO projet_boutique.BANK_GROUP (Type_compte, prenom, nom, mdp, solde) VALUES
    ('Boutique', 'Chic_Mode', 'Boutique1', 1234, 50000),
    ('Boutique', 'Class', 'Boutique2', 5678, 80000),
    ('Boutique', 'Chez Diop', 'Boutique3', 9012, 65000);

-- Particuliers
INSERT INTO projet_boutique.BANK_GROUP (Type_compte, prenom, nom, mdp, solde) VALUES
    ('Particulier', 'Amadou', 'Diop', 1111, 300000),
    ('Particulier', 'Aïssatou', 'Sow', 2222, 450000),
    ('Particulier', 'Kwame', 'Appiah', 3333, 600000),
    ('Particulier', 'Fatoumata', 'Diallo', 4444, 350000),
    ('Particulier', 'Ibrahim', 'Traoré', 5555, 700000),
    ('Particulier', 'Amina', 'Toure', 6666, 550000),
    ('Particulier', 'Abdoulaye', 'Barry', 7777, 400000),
    ('Particulier', 'Kadiatou', 'Camara', 8888, 750000),
    ('Particulier', 'Boubacar', 'Keïta', 9999, 480000),
    ('Particulier', 'Aïcha', 'Konaté', 1010, 520000),
    ('Particulier', 'Samba', 'Ndiaye', 1212, 680000),
    ('Particulier', 'Aïssatou', 'Diallo', 1313, 610000);



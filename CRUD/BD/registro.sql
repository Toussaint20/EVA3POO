DROP SCHEMA IF EXISTS `agenda` ;
CREATE SCHEMA IF NOT EXISTS `agenda`   ;
USE `agenda` ;
 

-- -----------------------------------------------------
-- Table `feria`.`comunas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Registro` ;

CREATE TABLE IF NOT EXISTS `Registro` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(64) NOT NULL,
  `Telefono` int(9) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO `Registro`(`Nombre`, `Telefono`) VALUES
('Juan', 99750000),
('Maria',93405835),
('Karina',90242342),
('Marta',98234234)

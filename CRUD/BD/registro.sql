DROP SCHEMA IF EXISTS `courier` ;
CREATE SCHEMA IF NOT EXISTS `courier`   ;
USE `courier` ;
 

-- -----------------------------------------------------
-- sql para el courier
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Registro` ;

CREATE TABLE IF NOT EXISTS `Registro` (
  'Id' int(11) NOT NULL AUTO_INCREMENT,
  'Destinatario' varchar(64) NOT NULL,
  'Direccion' varchar(64) NOT NULL,
  'C_origen' varchar(64) NOT NULL,
  'C_destino' varchar(64) NOT NULL,
  'Peso' int(9) NOT NULL,

  PRIMARY KEY ('Id')
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO 'Registro'('Nombre', 'Direccion', 'C_origen', 'C_destino', 'Peso',) VALUES
('John Cena', 'Pablo Neruda 331', 'Santiago', 'Rancagua', '66'),
('Tomás Cid', 'Blanco Encalada 210', 'Tokyo', 'Gorbea', '44.5'),
('Tokoyami Towa', 'Hololive Corp 241', 'Gorbea', 'Tokyo', '44.5'),
('Elton Jon', 'Los Poetas 345', 'Valdivia', 'Puerto Mont', '223'),
('Keanu Reeves', 'Pasaje Vega 02147', 'Santiago', 'Temuco', '12')

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 05-11-2023 a las 19:14:10
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `courier`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro`
--

DROP TABLE IF EXISTS `registro`;
CREATE TABLE IF NOT EXISTS `registro` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Destinatario` varchar(64) NOT NULL,
  `Direccion` varchar(64) NOT NULL,
  `C_origen` varchar(64) NOT NULL,
  `C_destino` varchar(64) NOT NULL,
  `Peso` int NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `registro`
--

INSERT INTO `registro` (`Id`, `Destinatario`, `Direccion`, `C_origen`, `C_destino`, `Peso`) VALUES
(1, 'Tomas Cid', 'Blanco Encalada 210', 'Tokyo', 'Gorbea', 45),
(2, 'John Cena', 'Pluton 654', 'Santiago', 'Rancagua', 200),
(3, 'Tokoyami Towa', 'Hololive Corp 241', 'Gorbea', 'Tokyo', 45),
(4, 'Elton Jon', 'Los Poetas 345', 'Valdivia', 'Puerto Montt', 32),
(5, 'Keanu Reeves', 'Pasaje Vega 02147', 'Santiago', 'Temuco', 15);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuario` varchar(25) NOT NULL,
  `password` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usuario`, `password`) VALUES
('Admin', '202cb962ac59075b964b07152d234b70'),
('KurtCobain', '17f956b3682068879cc1aec7576f0874'),
('SONIC', 'c492e2055c443b958f77121954274958'),
('TheSilent', '3395f8341de86d74eec6921562f49ca5'),
('TMT26', 'ac9d7246c37cd747bfc16faf27009255');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

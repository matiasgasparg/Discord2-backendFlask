-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: discord2
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `servidor`
--

DROP TABLE IF EXISTS `servidor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servidor` (
  `idservidor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idservidor`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servidor`
--

LOCK TABLES `servidor` WRITE;
/*!40000 ALTER TABLE `servidor` DISABLE KEYS */;
INSERT INTO `servidor` VALUES (24,'Servidor Prueba','descripcion prueba'),(25,'Servidor Sinn','Sinn'),(26,'Servidor Matias','matias'),(27,'Servidor Prueba busqueda 1','Servidor Prueba busqueda 1'),(28,'Servidor Prueba busqueda 2','Servidor Prueba busqueda 2'),(29,'Servidor Prueba busqueda 2','Servidor Prueba busqueda 2'),(30,'Servidor Prueba busqueda 3','Servidor Prueba busqueda 3'),(31,'Servidor Prueba busqueda 4','Servidor Prueba busqueda 4'),(32,'Servidor Prueba busqueda 5','Servidor Prueba busqueda 5'),(33,'Servidor Prueba busqueda 6','Servidor Prueba busqueda 6'),(34,'Servidor Prueba busqueda 7','Servidor Prueba busqueda 8'),(35,'Servidor Prueba busqueda 9','Servidor Prueba busqueda 9'),(36,'a','a'),(37,'a','a'),(38,'a','a'),(39,'b','b'),(40,'as','as'),(41,'asdasdasd','asdasdads'),(42,'a','a'),(43,'Nuevo serviro','sadas'),(44,'PRUEBAZSÑDKASÑLDKAS','asdasdsadasdas'),(45,'PRUEBAZSÑDKASÑLDKAS','asdasdsadasdas'),(46,'PRUEBAZSÑDKASÑLDKAS','asdasdsadasdas'),(47,'PRUEBAZSÑDKASÑLDKAS','asdasdsadasdas'),(48,'PRUEBAZSÑDKASÑLDKAS','asdasdsadasdas'),(49,'a','a'),(50,'asd','asd'),(51,'zdx','s'),(52,'A','A'),(53,'PRUEBA DE REPRUEBA','AAA');
/*!40000 ALTER TABLE `servidor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-28  0:39:24

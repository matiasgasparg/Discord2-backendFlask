CREATE DATABASE  IF NOT EXISTS `discord2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `discord2`;
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
-- Table structure for table `canales`
--

DROP TABLE IF EXISTS `canales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canales` (
  `idcanal` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcanal`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canales`
--

LOCK TABLES `canales` WRITE;
/*!40000 ALTER TABLE `canales` DISABLE KEYS */;
INSERT INTO `canales` VALUES (25,'Canal prueba'),(26,'Canal con mensaje'),(27,'Segundo canal'),(28,'Canal prueba 2'),(29,'Prueba usuario 5'),(30,'Prueba canal2'),(31,'sss'),(32,'A'),(33,'b'),(34,'aaa'),(35,'a'),(36,'a'),(37,'asd'),(38,'a'),(39,'as'),(40,'xxxxxxxx'),(41,'ASD'),(42,'asd'),(43,'Cas'),(44,'asd'),(45,'asd'),(46,'aaaaaa'),(47,'xxxxxxaaa'),(48,'asdddd'),(49,'asdsd'),(50,'xxxxxxxxxxxx'),(51,'{'),(52,'b'),(53,'ñ'),(54,'ll'),(55,'ss'),(56,'a'),(57,'ccccccc'),(58,'w'),(59,'xza'),(60,'s'),(61,'dd'),(62,'a'),(63,'b'),(64,'c'),(65,'d'),(66,'d'),(67,'e'),(68,'f'),(69,'g'),(70,'x'),(71,'a'),(72,'b'),(73,'c'),(74,'d'),(75,'as'),(76,'a'),(77,'atttt'),(78,'ASD'),(79,'s'),(80,'aa'),(81,'s'),(82,'s'),(83,'SSSSSS'),(84,'asd'),(85,'Canal para el usuario 11 y servidor 40'),(86,'Canal para el usuario 11 y servidor 40'),(87,'Canal para el usuario 11 y servidor 40'),(88,'z'),(89,'c'),(90,'PRUEBA DE REPRUEBA'),(91,'asd'),(92,'asd');
/*!40000 ALTER TABLE `canales` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29  0:14:41

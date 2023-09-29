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
-- Table structure for table `id_canal_servidor`
--

DROP TABLE IF EXISTS `id_canal_servidor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `id_canal_servidor` (
  `idcanalservidor` int NOT NULL AUTO_INCREMENT,
  `idsv` int NOT NULL,
  `idcanal` int NOT NULL,
  PRIMARY KEY (`idcanalservidor`),
  KEY `fk_idsv_idx` (`idsv`),
  KEY `fk_idcanal_idx` (`idcanal`),
  CONSTRAINT `fk_idcanal` FOREIGN KEY (`idcanal`) REFERENCES `canales` (`idcanal`),
  CONSTRAINT `fk_idsv` FOREIGN KEY (`idsv`) REFERENCES `servidor` (`idservidor`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `id_canal_servidor`
--

LOCK TABLES `id_canal_servidor` WRITE;
/*!40000 ALTER TABLE `id_canal_servidor` DISABLE KEYS */;
INSERT INTO `id_canal_servidor` VALUES (1,24,41),(2,26,42),(3,27,43),(4,30,44),(5,38,45),(6,26,46),(7,26,47),(8,26,48),(9,26,49),(10,26,50),(11,26,51),(12,39,52),(13,37,53),(14,26,54),(15,26,55),(16,26,56),(17,26,57),(18,26,58),(19,26,59),(20,28,60),(21,28,61),(22,35,62),(23,35,63),(24,35,64),(25,35,65),(26,35,66),(27,35,67),(28,35,68),(29,35,69),(30,35,70),(31,34,71),(32,34,72),(33,34,73),(34,34,74),(35,40,75),(36,37,76),(37,41,77),(38,32,78),(39,26,79),(40,33,80),(41,42,81),(42,42,82),(43,42,83),(44,43,84),(45,40,85),(46,40,86),(47,40,87),(48,51,88),(49,25,89),(50,53,90),(51,44,91),(52,24,92);
/*!40000 ALTER TABLE `id_canal_servidor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29  0:14:42

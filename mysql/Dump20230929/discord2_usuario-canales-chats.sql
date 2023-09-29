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
-- Table structure for table `usuario-canales-chats`
--

DROP TABLE IF EXISTS `usuario-canales-chats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario-canales-chats` (
  `idusuario-canales-chats` int NOT NULL AUTO_INCREMENT,
  `iduser` int NOT NULL,
  `idcanal` int NOT NULL,
  `idchat` int NOT NULL,
  PRIMARY KEY (`idusuario-canales-chats`),
  KEY `fk_usertrio_idx` (`iduser`),
  KEY `fk_canaltrio_idx` (`idcanal`),
  KEY `fk_idchat_idx` (`idchat`),
  CONSTRAINT `fk_canaltrio` FOREIGN KEY (`idcanal`) REFERENCES `canales` (`idcanal`),
  CONSTRAINT `fk_idchat` FOREIGN KEY (`idchat`) REFERENCES `chat` (`idchat`) ON DELETE CASCADE,
  CONSTRAINT `fk_usertrio` FOREIGN KEY (`iduser`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario-canales-chats`
--

LOCK TABLES `usuario-canales-chats` WRITE;
/*!40000 ALTER TABLE `usuario-canales-chats` DISABLE KEYS */;
INSERT INTO `usuario-canales-chats` VALUES (1,5,41,59),(3,4,43,61),(4,4,43,62),(5,4,43,63),(6,4,45,64),(7,4,45,65),(8,4,45,66),(9,4,45,67),(10,4,48,68),(11,4,48,69),(12,4,52,70),(13,4,52,71),(14,4,45,72),(15,4,45,73),(16,4,51,74),(17,4,51,75),(18,4,51,76),(19,4,51,77),(20,4,54,78),(21,4,54,79),(22,4,54,80),(23,4,54,81),(24,4,54,82),(25,4,55,83),(26,4,59,84),(27,4,58,85),(28,4,59,86),(29,4,58,87),(31,4,46,89),(32,4,46,90),(33,4,60,91),(34,4,61,92),(35,4,61,93),(36,4,61,94),(37,4,61,95),(38,4,60,96),(39,4,61,97),(40,4,54,98),(41,4,51,99),(42,4,55,100),(43,4,62,101),(44,4,63,102),(45,4,63,103),(46,4,63,104),(47,4,64,105),(48,4,64,106),(49,4,64,107),(50,4,64,108),(51,4,66,109),(52,4,67,110),(53,4,68,111),(54,4,69,112),(55,4,69,113),(56,4,68,114),(57,4,69,115),(58,4,68,116),(59,4,70,117),(60,4,71,118),(61,4,72,119),(62,4,73,120),(63,4,73,121),(64,4,72,122),(65,4,74,123),(66,4,74,124),(67,4,74,125),(68,4,73,126),(69,4,72,127),(70,4,71,128),(71,4,42,129),(72,4,76,130),(73,4,76,131),(75,4,57,133),(76,4,57,134),(77,4,41,135),(78,4,41,136),(79,4,77,137),(80,4,77,138),(81,4,67,139),(82,4,67,140),(83,4,67,141),(84,4,67,142),(85,4,70,143),(86,4,78,144),(87,4,78,145),(88,4,42,146),(89,4,42,147),(90,4,42,148),(91,4,79,149),(92,4,80,150),(93,4,56,151),(94,4,50,152),(95,4,42,153),(96,5,42,154),(97,5,41,155),(98,4,77,156),(99,8,81,157),(100,8,83,158),(101,8,82,159),(102,8,82,160),(103,11,84,161),(104,11,41,162),(105,15,87,163),(106,18,43,164),(107,18,45,164),(108,18,88,165),(109,18,90,166),(110,18,91,167),(111,18,91,168),(112,11,84,169),(113,11,89,170),(114,5,92,171);
/*!40000 ALTER TABLE `usuario-canales-chats` ENABLE KEYS */;
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

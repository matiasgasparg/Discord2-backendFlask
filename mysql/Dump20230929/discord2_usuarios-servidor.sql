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
-- Table structure for table `usuarios-servidor`
--

DROP TABLE IF EXISTS `usuarios-servidor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios-servidor` (
  `iduserserver` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `id_server` int NOT NULL,
  PRIMARY KEY (`iduserserver`),
  KEY `fk_servidor_idx` (`id_server`) /*!80000 INVISIBLE */,
  KEY `fk_usuario_idx` (`id_user`),
  CONSTRAINT `fk_servidor` FOREIGN KEY (`id_server`) REFERENCES `servidor` (`idservidor`),
  CONSTRAINT `fk_usuario` FOREIGN KEY (`id_user`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios-servidor`
--

LOCK TABLES `usuarios-servidor` WRITE;
/*!40000 ALTER TABLE `usuarios-servidor` DISABLE KEYS */;
INSERT INTO `usuarios-servidor` VALUES (1,5,24),(2,5,25),(3,4,26),(4,4,24),(5,4,27),(6,4,28),(7,4,29),(8,4,30),(9,4,31),(10,4,32),(11,4,33),(12,4,34),(13,4,35),(14,5,26),(15,5,27),(16,5,28),(17,5,29),(18,5,30),(19,5,31),(20,5,32),(21,5,33),(22,5,34),(23,10,36),(24,4,37),(25,4,38),(26,4,39),(27,4,40),(28,4,41),(29,8,42),(30,11,43),(31,11,24),(32,11,45),(33,11,46),(34,11,47),(35,11,48),(36,11,38),(37,11,40),(38,5,40),(39,5,49),(40,5,50),(41,18,51),(42,18,52),(43,18,25),(44,18,49),(45,18,31),(46,18,29),(47,18,28),(48,18,24),(49,18,30),(50,18,47),(51,18,27),(52,18,50),(53,18,53),(54,18,44),(55,18,26),(56,11,50),(57,11,25),(58,4,52),(59,4,25);
/*!40000 ALTER TABLE `usuarios-servidor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29  0:14:40

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
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat` (
  `idchat` int NOT NULL AUTO_INCREMENT,
  `mensaje` text,
  `fecha_hora` datetime DEFAULT NULL,
  PRIMARY KEY (`idchat`)
) ENGINE=InnoDB AUTO_INCREMENT=173 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES (59,'ASD','2023-08-08 19:43:36'),(61,'Cas','2023-08-10 17:26:15'),(62,'Cas','2023-08-10 17:26:39'),(63,'asdx|','2023-08-10 17:28:00'),(64,'asd','2023-08-10 17:28:16'),(65,'asd','2023-08-10 17:28:22'),(66,'asdx','2023-08-10 17:28:26'),(67,'asdx','2023-08-10 17:28:27'),(68,'asd','2023-08-10 17:39:30'),(69,'cccc','2023-08-10 17:39:36'),(70,'b','2023-08-10 17:43:22'),(71,'b','2023-08-10 17:43:27'),(72,'b','2023-08-10 17:43:31'),(73,'b','2023-08-10 17:43:40'),(74,'b','2023-08-10 17:43:47'),(75,'b','2023-08-10 17:43:51'),(76,'b','2023-08-10 17:43:54'),(77,'b','2023-08-10 17:43:57'),(78,'bxxx','2023-08-10 17:44:05'),(79,'ssss','2023-08-10 17:44:28'),(80,'s','2023-08-10 17:44:32'),(81,'s','2023-08-10 17:44:35'),(82,'s','2023-08-10 17:44:36'),(83,'s','2023-08-10 17:44:44'),(84,'asd','2023-08-10 18:08:06'),(85,'asd','2023-08-10 18:08:17'),(86,'xxxxxxxxxxxxxxxxx','2023-08-10 18:08:22'),(87,'xxxxxxxxxxxxxxxxx','2023-08-10 18:08:25'),(89,'xxxxxxxxaaaaaaaaaaaxxxxxxx','2023-08-10 18:08:30'),(90,'prueba1\'','2023-08-10 18:08:31'),(91,'asd','2023-08-10 18:14:49'),(92,'asdxxx','2023-08-10 18:14:55'),(93,'asdxxx','2023-08-10 18:14:55'),(94,'asdxxx','2023-08-10 18:15:50'),(95,'asdxxx65\n','2023-08-10 18:15:55'),(96,'asdxxx653\n','2023-08-10 18:15:59'),(97,'asdxxx6535\n\n','2023-08-10 18:16:03'),(98,'ASDSAD','2023-08-10 18:20:44'),(99,'asdxxx6535\n\n','2023-08-10 18:20:49'),(100,'asdxxx6535\n\n','2023-08-10 18:20:51'),(101,'a','2023-08-10 18:21:05'),(102,'b','2023-08-10 18:21:11'),(103,'b','2023-08-10 18:21:11'),(104,'b','2023-08-10 18:21:14'),(105,'c','2023-08-10 18:21:20'),(106,'c','2023-08-10 18:21:23'),(107,'d','2023-08-10 18:21:30'),(108,'d','2023-08-10 18:21:30'),(109,'d','2023-08-10 18:21:35'),(110,'e','2023-08-10 18:21:41'),(111,'f','2023-08-10 18:21:49'),(112,'g','2023-08-10 18:21:53'),(113,'gs','2023-08-10 18:22:00'),(114,'gs','2023-08-10 18:22:03'),(115,'gs','2023-08-10 18:22:05'),(116,'gsa','2023-08-10 18:22:08'),(117,'a','2023-08-10 18:22:15'),(118,'a','2023-08-10 18:22:32'),(119,'b','2023-08-10 18:22:39'),(120,'c','2023-08-10 18:22:43'),(121,'c','2023-08-10 18:22:46'),(122,'c','2023-08-10 18:22:48'),(123,'d','2023-08-10 18:22:54'),(124,'d','2023-08-10 18:22:57'),(125,'da','2023-08-10 18:23:00'),(126,'ca','2023-08-10 18:23:02'),(127,'ca','2023-08-10 18:23:05'),(128,'aa','2023-08-10 18:23:08'),(129,'aa','2023-08-10 18:23:28'),(130,'asd','2023-08-10 18:25:45'),(131,'df','2023-08-10 18:25:55'),(133,'asd','2023-08-10 20:09:14'),(134,'asd','2023-08-10 20:09:17'),(135,'ASD','2023-08-10 20:09:43'),(136,'AAA','2023-08-10 20:09:46'),(137,'asdddd','2023-08-10 20:37:02'),(138,'asd','2023-08-10 20:37:06'),(139,'asd','2023-08-10 20:45:49'),(140,'asdsadasdsd','2023-08-10 20:45:50'),(141,'sssssssssssssssaaaaaaaaa','2023-08-10 20:45:53'),(142,'axcxacxacaxc','2023-08-10 20:45:56'),(143,'axxxxxxxx','2023-08-10 20:46:14'),(144,'ASDDDD','2023-08-10 21:02:38'),(145,'AAAAAAA','2023-08-10 21:02:39'),(146,'asdsss','2023-08-10 21:06:41'),(147,'aaaaaaaaaaaaaaaa','2023-08-10 21:07:14'),(148,'as','2023-08-10 21:07:17'),(149,'a','2023-08-11 11:26:28'),(150,'aa','2023-08-11 11:30:00'),(151,'xxx','2023-08-11 11:34:41'),(152,'sssssxxxxxx','2023-08-11 12:03:49'),(153,'xxxxxxxx','2023-08-11 12:04:04'),(154,'asd12','2023-08-11 12:06:23'),(155,'assss','2023-08-11 12:09:03'),(156,'ccc','2023-08-11 12:32:27'),(157,'asd','2023-08-13 18:42:29'),(158,'aaaaaaaa','2023-08-13 18:51:57'),(159,'AAAAAA','2023-08-13 19:05:18'),(160,'321656','2023-08-13 19:05:31'),(161,'asd','2023-08-13 19:27:57'),(162,'sad','2023-08-13 19:31:23'),(163,'EDITsss para el usuario 11 y servidor 40','2023-09-18 17:24:35'),(164,'EDITADO','2023-09-18 18:42:49'),(165,'HOLA CHYNTIA\n','2023-09-18 19:21:57'),(166,'asd','2023-09-18 19:24:28'),(167,'asd','2023-09-18 20:27:41'),(168,'sss','2023-09-18 20:28:20'),(169,'ded','2023-09-18 20:43:54'),(170,'sd','2023-09-18 22:50:58'),(171,'asdsss','2023-09-19 19:21:22');
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-29  0:14:43

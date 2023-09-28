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
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `datebirth` date NOT NULL,
  `img_perfil` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (4,'Matias Gaspar','Matiasgasparg','matias@gmail.com','contraseña','1997-02-03','http://127.0.0.1:5000/get_image/4_jabonsol.jpg'),(5,'Matts','Sinn','sinn@gmail.com','Patoganzo97','1998-03-03','/5_bollos.jpeg'),(6,'Lore','admin','admin','admin','1998-05-03','http://127.0.0.1:5000/get_image/6_824c42789a4b452327e5475a061b6061.jpg'),(7,'a','sinn@gmail.com','a','contraseña','1997-03-02',NULL),(8,'Matias','sinn','sinn@gmail.com','contraseña','1997-03-02','http://127.0.0.1:5000/get_image/8_jabonsol.jpg'),(9,'Matias','sinn','sinn@gmail.com','contraseña','1997-03-02',NULL),(10,'Matias','Lol','lol@gmail.com','contraseña','1997-03-02',NULL),(11,'Prueba','prueba','Prueba@gmail.com','contraseña','1997-03-02','http://127.0.0.1:5000/users/get_image/11_824c42789a4b452327e5475a061b6061.jpg'),(12,'Matias','johndoe123','johndoe@example.com','mysecretpassword','1990-05-15','profile_pic.jpg'),(15,'John DoSSSSe','DoSSSSe','johndssssoe@example.com','321321654','1990-01-01','profile.jpg'),(16,'asdasdasd asdasdasd','asdasdasdsa','asdasdsa@example.com','321321654','1990-01-01',NULL),(17,'s sa','s s','aaaaa@example.com','321321654','1990-01-01',NULL),(18,'asdsss','xxx','asssssds@gmail.com','asdsss','1997-03-02',NULL),(19,'prueba22','prueba22','prueba22@gmail.com','prueba22','1997-03-02',NULL),(20,'matiasgasparg','luis','luis@gmail.com','luis@gmail.com','1997-03-02',NULL),(21,'slkdajsalkdjas','asldkjklasdj','alskdjlkasd@galskjdlaksjd','alskdjlkasjd','1997-02-02',NULL),(22,'asdlñkjasldkjsa','lkjasldkjaslkdj','laskjdlkasjd','lkjaslkdjlaskd','1111-12-02',NULL),(23,'aaaaaaaaaaaaaaa','aaaaaaaaaaa','aaaaaaaaaa@gmail.com','aaaaaaaaaaaaaaaaaaa','1997-03-02',NULL),(24,'asdddddddddd','dddddddddddddddd','ddddddddddddddddddd','ddddddddddddddddd','2222-02-02',NULL),(25,'asdasd','dasdas','asdasdas','dasdasd','2222-02-22',NULL),(26,'asdasd','asdasd','asdasd','Matiasgaspaasdasdsarg','2222-02-02',NULL),(27,'aaaaaaa','aaaaaaaaaaaaaa','aaaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaaaaaaa','2222-02-22',NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-28  0:39:23

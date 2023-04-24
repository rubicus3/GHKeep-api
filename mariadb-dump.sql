-- MariaDB dump 10.19  Distrib 10.6.12-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: case_8
-- ------------------------------------------------------
-- Server version	10.6.12-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `fork`
--

DROP TABLE IF EXISTS `fork`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fork` (
  `state` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fork`
--

LOCK TABLES `fork` WRITE;
/*!40000 ALTER TABLE `fork` DISABLE KEYS */;
INSERT INTO `fork` VALUES (0);
/*!40000 ALTER TABLE `fork` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hum`
--

DROP TABLE IF EXISTS `hum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hum` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `id` int(11) DEFAULT NULL,
  `humidity` float DEFAULT NULL,
  `Tim` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hum`
--

LOCK TABLES `hum` WRITE;
/*!40000 ALTER TABLE `hum` DISABLE KEYS */;
INSERT INTO `hum` VALUES (1,1,77.2,'13:5'),(2,2,74.01,'13:5'),(3,3,69.86,'13:5'),(4,4,64.15,'13:5'),(5,5,72,'13:5'),(6,6,67.25,'13:5'),(7,1,68.61,'13:10'),(8,2,69.72,'13:10'),(9,3,68.64,'13:10'),(10,4,75.85,'13:10'),(11,5,71.93,'13:10'),(12,6,67.13,'13:10'),(13,1,72.78,'13:15'),(14,2,67.46,'13:15'),(15,3,69.06,'13:15'),(16,4,68.67,'13:15'),(17,5,66.87,'13:15'),(18,6,71.84,'13:15'),(19,1,65.81,'09:40'),(20,2,68.73,'09:40'),(21,3,69.01,'09:40'),(22,4,71.41,'09:40'),(23,5,67.83,'09:40'),(24,6,72.55,'09:40'),(25,1,76.7,'09:45'),(26,2,64.88,'09:45'),(27,3,67.5,'09:45'),(28,4,73.46,'09:45'),(29,5,65.62,'09:45'),(30,6,69.35,'09:45'),(31,1,66.67,'09:50'),(32,2,68.89,'09:50'),(33,3,70.86,'09:50'),(34,4,68.08,'09:50'),(35,5,67.83,'09:50'),(36,6,67.37,'09:50'),(37,1,73.37,'09:55'),(38,2,64.24,'09:55'),(39,3,65.7,'09:55'),(40,4,66.51,'09:55'),(41,5,68.6,'09:55'),(42,6,66.73,'09:55'),(43,1,78.89,'10:00'),(44,2,62.35,'10:00'),(45,3,71.46,'10:00'),(46,4,66.82,'10:00'),(47,5,66.99,'10:00'),(48,6,67.72,'10:00'),(49,1,61.06,'09:20'),(50,2,68.58,'09:20'),(51,3,70.24,'09:20'),(52,4,70.11,'09:20'),(53,5,69.89,'09:20'),(54,6,71.69,'09:20'),(55,1,72.45,'09:25'),(56,2,77.49,'09:25'),(57,3,75.36,'09:25'),(58,4,73.17,'09:25'),(59,5,74.86,'09:25'),(60,6,68.29,'09:25'),(61,1,74.27,'09:30'),(62,2,71.34,'09:30'),(63,3,63.42,'09:30'),(64,4,73.5,'09:30'),(65,5,65.83,'09:30'),(66,6,67.07,'09:30'),(67,1,64.76,'09:35'),(68,2,63.53,'09:35'),(69,3,76.29,'09:35'),(70,4,72.8,'09:35'),(71,5,66.95,'09:35'),(72,6,73.97,'09:35'),(73,1,63.52,'08:55'),(74,2,62.86,'08:55'),(75,3,70.53,'08:55'),(76,4,69.95,'08:55'),(77,5,71.83,'08:55'),(78,6,72.56,'08:55'),(79,1,64.46,'09:50'),(80,2,68.93,'09:50'),(81,3,76.01,'09:50'),(82,4,72.07,'09:50'),(83,5,70.11,'09:50'),(84,6,69.81,'09:50'),(85,1,62.03,'21:45'),(86,2,70.03,'21:45'),(87,3,75,'21:45'),(88,4,71.15,'21:45'),(89,5,65.8,'21:45'),(90,6,66.01,'21:45'),(91,1,61.74,'21:50'),(92,2,65.3,'21:50'),(93,3,70.17,'21:50'),(94,4,68.29,'21:50'),(95,5,69.85,'21:50'),(96,6,70.95,'21:50'),(97,1,78.85,'21:55'),(98,2,64.36,'21:55'),(99,3,69.34,'21:55'),(100,4,66.71,'21:55'),(101,5,74.6,'21:55'),(102,6,68.97,'21:55'),(103,1,78.06,'22:00'),(104,2,66.19,'22:00'),(105,3,75.29,'22:00'),(106,4,70.59,'22:00'),(107,5,72.02,'22:00'),(108,6,70.09,'22:00'),(109,1,62.31,'21:20'),(110,2,65.08,'21:20'),(111,3,74.29,'21:20'),(112,4,71.59,'21:20'),(113,5,68.55,'21:20'),(114,6,67.17,'21:20'),(115,1,76.84,'21:45'),(116,2,69.38,'21:45'),(117,3,71.34,'21:45'),(118,4,64.55,'21:45'),(119,5,67.41,'21:45'),(120,6,70.14,'21:45'),(121,1,69.94,'21:50'),(122,2,74.37,'21:50'),(123,3,69.76,'21:50'),(124,4,72.56,'21:50'),(125,5,67.17,'21:50'),(126,6,70.07,'21:50'),(127,1,75.93,'21:55'),(128,2,74.43,'21:55'),(129,3,69.2,'21:55'),(130,4,68.32,'21:55'),(131,5,72.52,'21:55'),(132,6,73.08,'21:55'),(133,1,78.75,'22:00'),(134,2,67.06,'22:00'),(135,3,68.3,'22:00'),(136,4,67.11,'22:00'),(137,5,74.06,'22:00'),(138,6,67.51,'22:00'),(139,1,75.67,'09:05'),(140,2,67.05,'09:05'),(141,3,72.88,'09:05'),(142,4,72.01,'09:05'),(143,5,71.61,'09:05'),(144,6,68.88,'09:05'),(145,1,75.9,'09:24'),(146,2,77.14,'09:24'),(147,3,63.73,'09:24'),(148,4,70.65,'09:24'),(149,5,70.47,'09:24'),(150,6,68.86,'09:24'),(151,1,76.63,'09:25'),(152,2,72.53,'09:25'),(153,3,68.72,'09:25'),(154,4,65.63,'09:25'),(155,5,65.27,'09:25'),(156,6,72.62,'09:25'),(157,1,72.81,'09:32'),(158,2,72.41,'09:32'),(159,3,66.67,'09:32'),(160,4,64.65,'09:32'),(161,5,69.51,'09:32'),(162,6,66.16,'09:32'),(163,1,63.26,'09:44'),(164,2,74.66,'09:44'),(165,3,69.24,'09:44'),(166,4,64.88,'09:44'),(167,5,69.65,'09:44'),(168,6,70.58,'09:44'),(169,1,60,'10:00'),(170,2,60,'10:00'),(171,3,60,'10:00'),(172,4,60,'10:00'),(173,5,60,'10:00'),(174,6,60,'10:00'),(175,1,1023,'15:47'),(176,1,1023,'15:48'),(177,1,0,'17:07'),(178,1,0,'17:08'),(179,1,49,'17:09'),(180,1,54,'17:10');
/*!40000 ALTER TABLE `hum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soil_warnings`
--

DROP TABLE IF EXISTS `soil_warnings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `soil_warnings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `humidity_soil` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soil_warnings`
--

LOCK TABLES `soil_warnings` WRITE;
/*!40000 ALTER TABLE `soil_warnings` DISABLE KEYS */;
INSERT INTO `soil_warnings` VALUES (1,70),(2,70),(3,60),(4,70),(5,60),(6,60);
/*!40000 ALTER TABLE `soil_warnings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp_hum`
--

DROP TABLE IF EXISTS `temp_hum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `temp_hum` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `id` int(11) DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `humidity` float DEFAULT NULL,
  `tim` varchar(8) DEFAULT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_hum`
--

LOCK TABLES `temp_hum` WRITE;
/*!40000 ALTER TABLE `temp_hum` DISABLE KEYS */;
INSERT INTO `temp_hum` VALUES (1,1,31.46,67.03,'13:5'),(2,2,30.35,51.74,'13:5'),(3,3,29.93,56.04,'13:5'),(4,4,29.95,72.03,'13:5'),(5,1,32.47,54.69,'13:10'),(6,2,29.42,51.46,'13:10'),(7,3,29.48,50.77,'13:10'),(8,4,29.84,45.29,'13:10'),(9,1,30.46,42.87,'13:15'),(10,2,27.72,57.51,'13:15'),(11,3,30.98,78.9,'13:15'),(12,4,29.04,83.42,'13:15'),(13,1,31.32,52.6,'09:40'),(14,2,31.57,75.67,'09:40'),(15,3,30.07,73.43,'09:40'),(16,4,29.83,55.76,'09:40'),(17,1,29.78,43.63,'09:45'),(18,2,31.93,39.68,'09:45'),(19,3,29.7,64.3,'09:45'),(20,4,29.97,70.58,'09:45'),(21,1,30.98,47.48,'09:50'),(22,2,28.42,63.92,'09:50'),(23,3,30.21,76.27,'09:50'),(24,4,29.45,71.66,'09:50'),(25,1,26.17,73.83,'09:55'),(26,2,29.58,66.43,'09:55'),(27,3,30.82,78.09,'09:55'),(28,4,29.25,74.88,'09:55'),(29,1,31.58,72.05,'10:00'),(30,2,27.82,56.27,'10:00'),(31,3,30.22,42.52,'10:00'),(32,4,29.88,55.03,'10:00'),(33,1,28.94,41.67,'09:20'),(34,2,31.94,70.38,'09:20'),(35,3,28.8,66.62,'09:20'),(36,4,29.85,69.24,'09:20'),(37,1,30.22,46.47,'09:25'),(38,2,31.09,58.36,'09:25'),(39,3,30.56,43.52,'09:25'),(40,4,29.22,62.86,'09:25'),(41,1,31.08,45.19,'09:30'),(42,2,27.79,66.85,'09:30'),(43,3,30.54,74.39,'09:30'),(44,4,29.08,41.93,'09:30'),(45,1,29.58,42.64,'09:35'),(46,2,31.38,61.71,'09:35'),(47,3,30.24,78.35,'09:35'),(48,4,29.37,60.96,'09:35'),(49,1,27.26,76.95,'08:55'),(50,2,27.45,62.81,'08:55'),(51,3,30.55,82.71,'08:55'),(52,4,29.56,68.33,'08:55'),(53,1,29.93,80.44,'09:50'),(54,2,28.67,54.44,'09:50'),(55,3,30.86,60.42,'09:50'),(56,4,29.47,68.35,'09:50'),(57,1,29.4,71.52,'21:45'),(58,2,31.81,40.78,'21:45'),(59,3,29.72,55.02,'21:45'),(60,4,29.86,63.39,'21:45'),(61,1,29,47.76,'21:50'),(62,2,28.52,72.39,'21:50'),(63,3,28.86,72.01,'21:50'),(64,4,29.98,77.07,'21:50'),(65,1,32.16,63.59,'21:55'),(66,2,28.89,46.58,'21:55'),(67,3,30.21,40.87,'21:55'),(68,4,29.91,38.94,'21:55'),(69,1,28.88,55.52,'22:00'),(70,2,30.87,40.67,'22:00'),(71,3,28.47,51.6,'22:00'),(72,4,29.41,82.67,'22:00'),(73,1,32.8,79.57,'21:20'),(74,2,29.9,81.89,'21:20'),(75,3,29.61,43.58,'21:20'),(76,4,29.68,81.16,'21:20'),(77,1,27.82,75.54,'21:45'),(78,2,30.74,57.34,'21:45'),(79,3,30.75,51.01,'21:45'),(80,4,29.75,37.06,'21:45'),(81,1,31.53,43.47,'21:50'),(82,2,31.56,42.64,'21:50'),(83,3,30.03,43.17,'21:50'),(84,4,29.92,48.33,'21:50'),(85,1,31.98,41.13,'21:55'),(86,2,29.14,67.9,'21:55'),(87,3,29.93,43.51,'21:55'),(88,4,29.06,70.29,'21:55'),(89,1,27.8,57.02,'22:00'),(90,2,31.31,46.8,'22:00'),(91,3,30.03,73.01,'22:00'),(92,4,29.78,45.17,'22:00'),(93,1,27.21,74.46,'09:05'),(94,2,30.64,63.67,'09:05'),(95,3,29.52,74.91,'09:05'),(96,4,29.53,73.27,'09:05'),(97,1,27.56,43.33,'09:10'),(98,2,27.54,78.26,'09:10'),(99,1,31.97,56.74,'09:16'),(100,2,28.08,49.49,'09:16'),(101,3,30.95,75.97,'09:16'),(102,4,29.04,56.91,'09:16'),(103,1,32.4,61.16,'09:16'),(104,2,30.33,73.76,'09:16'),(105,3,30.89,80.86,'09:16'),(106,4,29.75,60.87,'09:16'),(107,1,29.86,55.32,'09:18'),(108,2,29.08,76.6,'09:18'),(109,3,30.51,81.12,'09:18'),(110,4,29.21,65.65,'09:18'),(111,1,30.68,45.85,'09:18'),(112,2,31.2,53.6,'09:18'),(113,3,28.81,68.85,'09:18'),(114,4,29.04,70.49,'09:18'),(115,1,31.8,60.61,'09:32'),(116,2,31.81,62.12,'09:32'),(117,3,30.09,66.83,'09:32'),(118,4,29.04,64.63,'09:32'),(119,1,32.83,48.45,'09:32'),(120,2,31.93,71.95,'09:32'),(121,3,29.82,60.96,'09:32'),(122,4,29.19,51.53,'09:32'),(123,1,31.24,51.55,'09:44'),(124,2,29.89,54.57,'09:44'),(125,3,28.47,47.01,'09:44'),(126,4,29.22,64.01,'09:44'),(127,1,30,60,'10:00'),(128,2,30,60,'10:00'),(129,3,30,60,'10:00'),(130,4,30,60,'10:00'),(131,1,26.5,21,'15:47'),(132,2,26.3,16,'15:47'),(133,1,26.4,22,'15:48'),(134,2,26.1,17,'15:48'),(135,1,26.3,21,'15:49'),(136,2,25.7,15,'15:49'),(137,1,26.1,22,'15:50'),(138,2,25.4,16,'15:50'),(139,1,26.1,21,'15:51'),(140,2,25.3,15,'15:51'),(141,1,26.1,22,'15:53'),(142,2,25.3,16,'15:53'),(143,1,26,21,'15:55'),(144,2,25.3,16,'15:55'),(145,1,25.9,20,'15:56'),(146,2,25.2,15,'15:56'),(147,1,25.9,22,'15:57'),(148,2,25.4,17,'15:57'),(149,1,27.4,23,'17:07'),(150,2,27.7,17,'17:07'),(151,1,27.4,23,'17:08'),(152,2,27.6,17,'17:08'),(153,1,27.4,23,'17:09'),(154,2,27.7,17,'17:09'),(155,1,27.3,29,'17:10'),(156,2,27.6,17,'17:10');
/*!40000 ALTER TABLE `temp_hum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `total_hum`
--

DROP TABLE IF EXISTS `total_hum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `total_hum` (
  `state` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `total_hum`
--

LOCK TABLES `total_hum` WRITE;
/*!40000 ALTER TABLE `total_hum` DISABLE KEYS */;
INSERT INTO `total_hum` VALUES (0);
/*!40000 ALTER TABLE `total_hum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warnings`
--

DROP TABLE IF EXISTS `warnings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `warnings` (
  `temperature` float DEFAULT NULL,
  `humidity_air` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warnings`
--

LOCK TABLES `warnings` WRITE;
/*!40000 ALTER TABLE `warnings` DISABLE KEYS */;
INSERT INTO `warnings` VALUES (25,60);
/*!40000 ALTER TABLE `warnings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `watering`
--

DROP TABLE IF EXISTS `watering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `watering` (
  `id` int(11) DEFAULT NULL,
  `state` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `watering`
--

LOCK TABLES `watering` WRITE;
/*!40000 ALTER TABLE `watering` DISABLE KEYS */;
INSERT INTO `watering` VALUES (1,0),(2,1),(3,1),(4,0),(5,1),(6,1);
/*!40000 ALTER TABLE `watering` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'case_8'
--
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Change_fork` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Change_fork`()
begin
	set @st = 0;
	
	select state from case_8.fork f into @st;
	set @s = if(@st = 0, 1, 0);
	
	update case_8.fork 
	set state = @s;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Change_total_hum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Change_total_hum`()
begin
	set @st = 0;
	
	select state from case_8.total_hum th into @st;
	set @s = if(@st = 0, 1, 0);
	
	update case_8.total_hum 
	set state = @s;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Change_warnings_h` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Change_warnings_h`(
	hum float
)
begin
	update case_8.warnings 
	set humidity_air = hum;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Change_warnings_hb` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Change_warnings_hb`(
	i int,
	hb float
)
begin
	update case_8.soil_warnings  
	set humidity_soil = hb
	WHERE id like i;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Change_warnings_temp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Change_warnings_temp`(
	temp float
)
begin
	update case_8.warnings 
	set temperature = temp;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Change_watering` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Change_watering`(
	p_id int
)
begin
	set @st = 0;
	
	select state from case_8.watering w where id like p_id into @st;
	set @s = if(@st = 0, 1, 0);
	
	update case_8.watering 
	set state = @s
	where id like p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Create_fork` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Create_fork`()
begin
	set @s = '';
	select state from case_8.fork f limit 1 into @s;
	set @st = if(@s = '', 0, '');
	insert into fork
	(state)
	values
	(@st);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Create_hum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Create_hum`(
	p_id int,
	hum float,
	tim varchar(8)
)
begin
	insert into case_8.hum 
	(id, humidity, Tim)
	values
	(p_id, hum, tim);
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Create_soil_warnings` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Create_soil_warnings`()
BEGIN
	INSERT into case_8.soil_warnings 
	(humidity_soil)
	values
	(60.0);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Create_temp_hum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Create_temp_hum`(
	p_id int,
	temp float,
	hum float,
	tim varchar(8)
)
begin
	set @q = 0;	
	select COUNT(DISTINCT (id)) FROM case_8.temp_hum th into @q;

	set @a = 0;
	select a_id into @a from case_8.temp_hum th where id like p_id order by a_id desc limit 1;

	set @w = 0;
	select id from case_8.temp_hum th where a_id like (@a - 1) into @w;

	set @i = 0;
	if(@q = 0) then 
		set @i = 1;
	elseif p_id <> @w then
		set @i = 1;
	else
		set @i = p_id not in (select id from case_8.temp_hum th);
	end IF;
	IF(@i = 1)then
		insert into case_8.temp_hum 
		(id, temperature, humidity, tim)
		values
		(p_id, temp, hum, tim);
	end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Create_total_hum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Create_total_hum`()
begin
	set @s = '';
	select state from case_8.total_hum th limit 1 into @s;
	set @st = if(@s = '', 0, '');

	insert into case_8.total_hum 
	(state)
	values
	(@st);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Create_warnings` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Create_warnings`()
begin
	set @t = '';
	select temperature from case_8.warnings w limit 1 into @t;
	set @tem = if(@t = '', 30.0, '');

	set @h = '';
	select humidity_air from case_8.warnings w limit 1 into @h;
	set @hum = if(@h = '', 70.0, '');
	
	insert into case_8.warnings 
	(temperature, humidity_air)
	values
	(@tem, @hum);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Create_watering` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Create_watering`(
	p_id int
)
begin
	set @q = 0;	
	select COUNT(DISTINCT (id)) FROM case_8.watering into @q;
	set @i = if(@q = 0, 1, p_id not in (select id from case_8.watering w));
	IF(@i = 1)then
		insert into case_8.watering 
		(id, state)
		values
		(p_id, 0);
	end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_fork` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_fork`()
begin
	select state from case_8.fork;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_hum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_hum`(
	p_id int
)
BEGIN
	select * from case_8.hum where id = p_id order by a_id desc limit 5;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_hum_for_table` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_hum_for_table`(
	num int
)
BEGIN
	select humidity from case_8.hum order by a_id desc limit num;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_hum_from_temp_hum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_hum_from_temp_hum`(
	num int
)
begin
	select a_id, humidity, tim from case_8.temp_hum order by a_id desc limit num;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_hum_num` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_hum_num`()
BEGIN
	select id from case_8.hum order by a_id desc limit 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_hum_temp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_hum_temp`(
	p_id int
)
begin
	select * from case_8.temp_hum where id like p_id order by a_id desc limit 5;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_soil_warnings` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_soil_warnings`(
	i int
)
BEGIN
	SELECT * from case_8.soil_warnings WHERE id LIKE i;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_temp_from_temp_hum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_temp_from_temp_hum`(
	num int
)
begin
	select a_id, temperature, tim from case_8.temp_hum order by a_id desc limit num;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_temp_hum_for_table` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_temp_hum_for_table`(
	num int
)
BEGIN
	select temperature, humidity from case_8.temp_hum order by a_id desc limit num;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_temp_hum_num` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_temp_hum_num`()
BEGIN
	select id from case_8.temp_hum order by a_id desc limit 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_total_hum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_total_hum`()
begin
	select * from case_8.total_hum;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_warnings` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_warnings`()
begin
	select * from case_8.warnings;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Get_watering` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Get_watering`(
	p_id int
)
begin
	select * from case_8.watering where id like p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-24 17:12:03

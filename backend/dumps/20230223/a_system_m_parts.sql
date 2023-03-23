-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: 192.168.3.10    Database: a_system
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `m_parts`
--

DROP TABLE IF EXISTS `m_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `m_parts` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `pcid` int NOT NULL,
  `pcd` varchar(45) NOT NULL,
  `pname` varchar(45) NOT NULL,
  `ppname` varchar(45) NOT NULL,
  `prevision` varchar(45) DEFAULT NULL COMMENT 'リビジョン',
  `pvendor` varchar(45) DEFAULT NULL COMMENT '手配先',
  `ptype` varchar(45) DEFAULT NULL COMMENT '型式',
  `pmaterial` varchar(45) DEFAULT NULL,
  `pio` varchar(45) DEFAULT NULL,
  `pmtlmain_cost` int DEFAULT NULL,
  `pmtlsub_cost` int DEFAULT NULL,
  `pprocdict_cost` int DEFAULT NULL,
  `pprocsub_cost` int DEFAULT NULL,
  `toroku` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `kosin` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`pid`),
  KEY `cid_idx` (`pcid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `m_parts`
--

LOCK TABLES `m_parts` WRITE;
/*!40000 ALTER TABLE `m_parts` DISABLE KEYS */;
INSERT INTO `m_parts` VALUES (3,0,'string','string','string','string','string','string','string','string',0,0,0,0,'2023-01-19 22:36:20','2023-01-19 22:36:20'),(4,22,'ALD-A001Z000','タイヤ','タイヤ','A','1','A','A','A',0,0,0,0,'2023-01-19 22:53:43','2023-01-31 22:17:22'),(5,23,'ALD-A002Z000','ホイール','ホイール','A','A','A','A','A',0,0,0,0,'2023-01-19 22:54:14','2023-01-22 10:11:19'),(6,24,'ALD-A003Z000','ナット','ナット','1','1','清死','淳之介','3',1110,11002,232,23432,'2023-01-20 21:16:04','2023-01-22 10:11:55'),(7,25,'ALD-A001Y001','サスペンション','サスペンション','34','3','45','キンゾック','3',20,32,42,44,'2023-01-21 09:59:59','2023-01-22 10:12:16'),(8,26,'ALD-A001Y002','サスペンション（赤）','さす','','','','','',0,0,0,0,'2023-01-22 10:13:08','2023-01-22 10:13:08'),(9,27,'ALD-A001Y003','サスペンション（青）','','','','','','',0,0,0,0,'2023-01-22 10:13:16','2023-01-22 10:13:16'),(10,31,'CNQ-A001Z000','AAA','AAA','SSSS','1','１２３','鉄','1',1,2,3,4,'2023-01-27 13:13:27','2023-01-27 13:13:27');
/*!40000 ALTER TABLE `m_parts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-23 17:31:26

-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: demo
-- ------------------------------------------------------
-- Server version	5.5.62

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cart` (
  `product_id` int(11) DEFAULT NULL,
  `mrp` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_item`
--

DROP TABLE IF EXISTS `order_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_item` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cart_id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_item`
--

LOCK TABLES `order_item` WRITE;
/*!40000 ALTER TABLE `order_item` DISABLE KEYS */;
INSERT INTO `order_item` VALUES (1,1,3,1,1,'2020-12-30 05:50:58'),(2,2,3,1,1,'2020-12-30 06:15:33'),(3,2,26,1,11,'2020-12-30 06:15:33'),(4,2,27,1,2,'2020-12-30 06:15:33'),(5,2,21,1,32,'2020-12-30 06:15:33'),(6,2,6,1,32,'2020-12-30 06:15:33'),(7,2,34,1,190,'2020-12-30 06:15:33'),(8,3,34,1,100,'2020-12-30 06:25:56'),(9,4,34,1,100,'2020-12-30 07:03:09'),(10,5,34,1,100,'2020-12-30 07:03:11'),(11,6,34,4,100,'2020-12-30 16:37:33'),(12,6,32,4,12,'2020-12-30 16:37:33'),(13,6,7,4,150,'2020-12-30 16:37:33'),(14,6,2,4,10,'2020-12-30 16:37:33'),(15,6,28,4,50,'2020-12-30 16:37:33'),(16,7,34,7,100,'2021-01-01 13:00:45'),(17,7,32,7,12,'2021-01-01 13:00:45'),(18,7,7,7,150,'2021-01-01 13:00:45'),(19,7,2,7,10,'2021-01-01 13:00:45'),(20,7,28,7,50,'2021-01-01 13:00:45'),(21,7,19,7,300,'2021-01-01 13:00:45'),(22,7,33,7,0,'2021-01-01 13:00:45'),(23,8,2,8,50,'2021-01-01 15:40:09'),(24,8,3,8,20,'2021-01-01 15:40:09'),(25,8,4,8,70,'2021-01-01 15:40:09'),(26,8,5,8,30,'2021-01-01 15:40:09'),(27,8,6,8,20,'2021-01-01 15:40:09'),(28,9,2,8,50,'2021-01-01 15:41:54'),(29,9,3,8,20,'2021-01-01 15:41:54'),(30,9,4,8,70,'2021-01-01 15:41:54'),(31,9,5,8,30,'2021-01-01 15:41:54'),(32,9,6,8,20,'2021-01-01 15:41:54'),(33,10,2,8,50,'2021-01-01 15:48:00'),(34,10,3,8,20,'2021-01-01 15:48:00'),(35,10,4,8,70,'2021-01-01 15:48:00'),(36,10,5,8,30,'2021-01-01 15:48:00'),(37,10,6,8,10,'2021-01-01 15:48:00'),(38,11,2,8,50,'2021-01-02 06:58:28'),(39,11,3,8,2,'2021-01-02 06:58:28'),(40,11,4,8,70,'2021-01-02 06:58:28'),(41,11,5,8,30,'2021-01-02 06:58:28'),(42,11,6,8,10,'2021-01-02 06:58:28'),(43,12,2,8,50,'2021-01-02 07:00:14'),(44,12,3,8,2,'2021-01-02 07:00:14'),(45,12,4,8,70,'2021-01-02 07:00:14'),(46,12,5,8,30,'2021-01-02 07:00:14'),(47,12,6,8,1,'2021-01-02 07:00:14'),(48,13,2,8,1,'2021-01-02 07:01:31'),(49,13,6,8,2,'2021-01-02 07:01:31'),(50,14,31,8,1,'2021-01-02 07:02:57'),(51,15,7,9,100,'2021-01-02 07:35:26'),(52,15,33,9,1,'2021-01-02 07:35:26'),(53,16,21,10,33,'2021-01-03 12:23:01');
/*!40000 ALTER TABLE `order_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `grand_total` float(10,2) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,299.00,'2020-12-30 05:50:58'),(2,1,29872.00,'2020-12-30 06:15:33'),(3,1,11000.00,'2020-12-30 06:25:56'),(4,1,11000.00,'2020-12-30 07:03:09'),(5,1,11000.00,'2020-12-30 07:03:11'),(6,4,23978.00,'2020-12-30 16:37:33'),(7,7,47678.00,'2021-01-01 13:00:45'),(8,8,18240.00,'2021-01-01 15:40:09'),(9,8,18240.00,'2021-01-01 15:41:54'),(10,8,17800.00,'2021-01-01 15:48:00'),(11,8,12418.00,'2021-01-02 06:58:28'),(12,8,12022.00,'2021-01-02 07:00:14'),(13,8,232.00,'2021-01-02 07:01:31'),(14,8,319.00,'2021-01-02 07:02:57'),(15,9,11959.00,'2021-01-02 07:35:26'),(16,10,8877.00,'2021-01-03 12:23:01');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `Product_id` int(11) NOT NULL AUTO_INCREMENT,
  `Product_name` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `Product_Qty` int(11) NOT NULL,
  `Product_price` float(10,2) NOT NULL,
  `category` varchar(102) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (2,'GUAVA',49,144.00,'FRUITS','2020-12-29 10:00:49'),(3,'STRAWBERRY',34,299.00,'FRUITS','2020-12-29 10:02:04'),(4,'ORANGE',1000,55.00,'FRUITS','2020-12-29 10:02:28'),(5,'WATERMELON',-50,11.00,'FRUITS','2020-12-29 10:03:15'),(6,'PINEAPPLE',5,44.50,'FRUITS','2020-12-29 10:04:26'),(7,'MILK 1 Kg',0,119.00,'DAIRY','2020-12-29 10:06:31'),(8,'APPLE',100,11.00,'FRUITS','2020-12-29 10:48:16'),(9,'PINE',55,120.00,'FRUITS','2020-12-29 10:49:19'),(10,'PRAYER FLAGS',100,120.00,'SIKKIM','2020-12-29 11:10:31'),(11,'PRAYER FLAGS',12,23.00,'SIKKIM','2020-12-30 04:18:54'),(12,'BOWLS',200,59.00,'SIKKIM','2020-12-30 06:00:36'),(13,'MASKS',20000,29.00,'SIKKIM','2020-12-30 06:01:06'),(14,'TEA',200,79.00,'SIKKIM','2020-12-30 06:01:28'),(15,'ORNAMENTS',200,1009.00,'SIKKIM','2020-12-30 06:01:52'),(16,'BOOKS',200,109.00,'SIKKIM','2020-12-30 06:02:01'),(17,'DRESS',200,999.00,'SIKKIM','2020-12-30 06:02:19'),(18,'MUSICAL INSTUMENTS',200,999.00,'SIKKIM','2020-12-30 06:03:11'),(19,'CARROT',0,79.00,'vegetables','2020-12-30 06:05:19'),(20,'POTATO',300,19.00,'vegetables','2020-12-30 06:05:32'),(21,'PEA',235,269.00,'vegetables','2020-12-30 06:05:51'),(22,'BEANS',300,49.00,'vegetables','2020-12-30 06:06:03'),(23,'ONION',300,99.00,'vegetables','2020-12-30 06:06:17'),(24,'CABBAGE',300,29.00,'vegetables','2020-12-30 06:06:46'),(25,'PEN',50,29.00,'stationary','2020-12-30 06:07:52'),(26,'PENCIL',39,59.00,'stationary','2020-12-30 06:08:18'),(27,'NOTEBOOK',48,49.00,'stationary','2020-12-30 06:08:33'),(28,'PENCIL COLOUR',1950,34.00,'stationary','2020-12-30 06:08:55'),(29,'PAINTING COLOUR',50,49.00,'stationary','2020-12-30 06:09:15'),(30,'RUBIC CUBE',50,89.00,'stationary','2020-12-30 06:09:32'),(31,'CHEEZ 1 KG',189,319.00,'dairy','2020-12-30 06:11:53'),(32,'PANEER 1 KG',166,249.00,'dairy','2020-12-30 06:12:47'),(33,'ICE CREAM 1 KG',189,59.00,'dairy','2020-12-30 06:13:15'),(34,'CURD 1 KG',-400,110.00,'dairy','2020-12-30 06:13:32'),(35,'CAKE 1 KG',190,109.00,'dairy','2020-12-30 06:13:49');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop`
--

DROP TABLE IF EXISTS `shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shop` (
  `SP_ID` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(30) DEFAULT NULL,
  `PASSWORD` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`SP_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop`
--

LOCK TABLES `shop` WRITE;
/*!40000 ALTER TABLE `shop` DISABLE KEYS */;
INSERT INTO `shop` VALUES (1,'A','1'),(2,'ANURAG','9798'),(3,'MRINAL','9791');
/*!40000 ALTER TABLE `shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `User_email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `User_phone` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `User_address` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_password` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `category` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `SP_ID` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'1','1','1','1','2020-12-29 11:49:55','1','Customer',NULL),(2,'S','1','1','1','2020-12-29 12:03:59','S',NULL,'S'),(3,'5','5','5','5','2020-12-30 04:23:58','5',NULL,NULL),(4,'mrinal','@','8**','delhi','2020-12-30 16:35:27','9791',NULL,NULL),(5,'ketan','k@s','9xxxxx','delhi','2020-12-30 16:46:03','9841',NULL,NULL),(6,'twinkle','td@','8xxxx','newdelhi','2020-12-30 16:46:44','9636',NULL,NULL),(7,'alok','a@k','00','delhi','2021-01-01 12:59:24','00',NULL,NULL),(8,'Aryanraj','aryanraj','9891759796','549,b2','2021-01-01 15:34:33','1122334455',NULL,NULL),(9,'mrs purvi','@','8','delhi','2021-01-02 07:34:34','1',NULL,NULL),(10,'hetal','@','0','p','2021-01-03 12:22:13','12',NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-11 19:14:00

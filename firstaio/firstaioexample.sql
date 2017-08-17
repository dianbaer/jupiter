/*
Navicat MySQL Data Transfer

Source Server         : localhost_3307
Source Server Version : 50505
Source Host           : localhost:3307
Source Database       : firstaioexample

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-08-14 14:34:44
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for example
-- ----------------------------
DROP TABLE IF EXISTS `example`;
CREATE TABLE `example` (
  `id` varchar(64) NOT NULL,
  `name` varchar(255) NOT NULL,
  `create_time` double NOT NULL,
  `status` tinyint(4) NOT NULL,
  `num` int(11) NOT NULL,
  `price` bigint(20) NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*
Navicat MySQL Data Transfer

Source Server         :  139.199.26.172
Source Server Version : 50722
Source Host           : 139.199.26.172:3306
Source Database       : sports

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2018-05-31 10:54:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `Badges`
-- ----------------------------
DROP TABLE IF EXISTS `Badges`;
CREATE TABLE `Badges` (
  `Id` int(8) NOT NULL,
  `UserId` int(8) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Date` varchar(255) NOT NULL,
  `Class` int(8) NOT NULL,
  `TagBased` varchar(20) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Badges
-- ----------------------------

-- ----------------------------
-- Table structure for `Comments`
-- ----------------------------
DROP TABLE IF EXISTS `Comments`;
CREATE TABLE `Comments` (
  `Id` int(8) NOT NULL,
  `PostId` int(8) NOT NULL,
  `Score` varchar(10) NOT NULL,
  `Text` varchar(255) NOT NULL,
  `CreationDate` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Comments
-- ----------------------------

-- ----------------------------
-- Table structure for `PostHistory`
-- ----------------------------
DROP TABLE IF EXISTS `PostHistory`;
CREATE TABLE `PostHistory` (
  `Id` int(10) NOT NULL,
  `PostHistoryTypeId` int(10) NOT NULL,
  `PostId` int(10) NOT NULL,
  `RevisionGUID` varchar(255) NOT NULL,
  `CreationDate` varchar(255) NOT NULL,
  `UserId` int(10) NOT NULL,
  `Text` varchar(500) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of PostHistory
-- ----------------------------

-- ----------------------------
-- Table structure for `PostLinks`
-- ----------------------------
DROP TABLE IF EXISTS `PostLinks`;
CREATE TABLE `PostLinks` (
  `Id` int(10) NOT NULL,
  `CreationDate` varchar(255) NOT NULL,
  `PostId` int(10) NOT NULL,
  `RelatedPostId` int(10) NOT NULL,
  `LinkTypeId` int(10) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of PostLinks
-- ----------------------------

-- ----------------------------
-- Table structure for `Posts`
-- ----------------------------
DROP TABLE IF EXISTS `Posts`;
CREATE TABLE `Posts` (
  `Id` int(10) NOT NULL,
  `PostTypeId` varchar(255) NOT NULL,
  `AcceptedAnswerId` int(10) NOT NULL,
  `CreationDate` int(10) NOT NULL,
  `Score` int(10) NOT NULL,
  `ViewCount` varchar(255) NOT NULL,
  `Body` varchar(500) NOT NULL,
  `OwnerUserId` varchar(255) NOT NULL,
  `LastEditorUserId` varchar(255) NOT NULL,
  `LastEditDate` varchar(255) NOT NULL,
  `LastActivityDate` varchar(255) NOT NULL,
  `Title` varchar(255) NOT NULL,
  `Tags` varchar(255) NOT NULL,
  `AnswerCount` int(10) NOT NULL,
  `CommentCount` int(10) NOT NULL,
  `FavoriteCount` int(10) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Posts
-- ----------------------------

-- ----------------------------
-- Table structure for `Tags`
-- ----------------------------
DROP TABLE IF EXISTS `Tags`;
CREATE TABLE `Tags` (
  `Id` int(10) NOT NULL,
  `TagName` varchar(255) NOT NULL,
  `Count` int(10) NOT NULL,
  `ExcerptPostId` int(10) NOT NULL,
  `WikiPostId` int(10) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Tags
-- ----------------------------

-- ----------------------------
-- Table structure for `Users`
-- ----------------------------
DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `Id` int(8) NOT NULL,
  `Reputation` int(8) NOT NULL,
  `CreationDate` varchar(255) NOT NULL,
  `DisplayName` varchar(255) NOT NULL,
  `LastAccessDate` varchar(8) NOT NULL,
  `WebsiteUrl` varchar(50) NOT NULL,
  `Location` varchar(50) NOT NULL,
  `AboutMe` varchar(255) NOT NULL,
  `Views` varchar(255) NOT NULL,
  `UpVotes` varchar(255) NOT NULL,
  `DownVotes` varchar(255) NOT NULL,
  `AccountId` varchar(20) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Users
-- ----------------------------

-- ----------------------------
-- Table structure for `Votes`
-- ----------------------------
DROP TABLE IF EXISTS `Votes`;
CREATE TABLE `Votes` (
  `Id` int(10) NOT NULL,
  `PostId` int(10) NOT NULL,
  `VoteTypeId` int(10) NOT NULL,
  `CreationDate` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Votes
-- ----------------------------

-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 
-- 伺服器版本: 10.1.37-MariaDB
-- PHP 版本： 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `amazon`
--

-- --------------------------------------------------------

--
-- 資料表結構 `amazon_order`
--

CREATE TABLE `amazon_order` (
  `order_id` varchar(18) DEFAULT NULL,
  `sender_name` text,
  `sender_address` text,
  `sender_contact` int(18) DEFAULT NULL,
  `receiver_name` text,
  `receiver_address` text,
  `receiver_contact` int(18) DEFAULT NULL,
  `postal_code` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `amazon_order`
--

INSERT INTO `amazon_order` (`order_id`, `sender_name`, `sender_address`, `sender_contact`, `receiver_name`, `receiver_address`, `receiver_contact`, `postal_code`) VALUES
('123456', 'Chris Paul', 'America Pool', 89648964, 'Chris Wong', 'Dean Street, London', 19898964, 'BR6EC1'),
('125689', 'Sally Sam', 'North Korea, 1999 Building', 99009900, 'Kelly Lam', '30F, 8 Connaught Place, Hong Kong', 26572999, 'BR6EC1'),
('127890', 'Pooh Ping', 'Beijing, China', 666666666, 'Donald Chump', '7 Columbus Avenue, New York, United States', 1802567289, '10001');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

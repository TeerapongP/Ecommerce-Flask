-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 01, 2022 at 02:03 PM
-- Server version: 8.0.17
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bookstore`
--
CREATE DATABASE IF NOT EXISTS `bookstore` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `bookstore`;

-- --------------------------------------------------------

--
-- Table structure for table `product_bestseller`
--

CREATE TABLE `product_bestseller` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_price` int(10) NOT NULL,
  `product_images` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_bestseller`
--

INSERT INTO `product_bestseller` (`product_id`, `product_name`, `product_price`, `product_images`) VALUES
(1, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 19', 55, 'pd1.png'),
(2, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 18', 55, 'pd2.png'),
(3, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 17', 55, 'pd3.png'),
(4, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 16', 55, 'pd4.png'),
(5, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 8', 55, 'pd5.png'),
(6, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 7', 55, 'pd6.png'),
(7, 'มิเอรุโกะจัง ใครว่าหนูเห็นผี เล่มที่ 1', 129, 'pd7.png'),
(8, 'มิเอรุโกะจัง ใครว่าหนูเห็นผี เล่มที่ 2', 129, 'pd8.png'),
(9, 'มิเอรุโกะจัง ใครว่าหนูเห็นผี เล่มที่ 3', 129, 'pd9.png'),
(10, 'มิเอรุโกะจัง ใครว่าหนูเห็นผี เล่มที่ 4', 129, 'pd10.png'),
(11, 'NO GAME NO LIFE เล่มที่ 1', 100, 'pd11.png'),
(12, 'NO GAME NO LIFE เล่มที่ 2', 100, 'pd12.png');

-- --------------------------------------------------------

--
-- Table structure for table `product_index`
--

CREATE TABLE `product_index` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_price` int(10) NOT NULL,
  `product_images` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_index`
--

INSERT INTO `product_index` (`product_id`, `product_name`, `product_price`, `product_images`) VALUES
(1, 'สารภาพรักกับคุณคางุยะซ ะดีๆ เล่มที่ 21', 55, 'pd1.png'),
(2, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 10', 55, 'pd2.png'),
(3, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 19', 55, 'pd3.png'),
(4, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 20', 55, 'pd4.png'),
(5, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 9', 55, 'pd5.png'),
(6, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 18', 55, 'pd6.png');

-- --------------------------------------------------------

--
-- Table structure for table `product_promotions`
--

CREATE TABLE `product_promotions` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_images` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `product_promotions`
--

INSERT INTO `product_promotions` (`product_id`, `product_name`, `product_price`, `product_images`) VALUES
(1, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 6', '44', 'pd1.png'),
(2, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 15', '44', 'pd2.png'),
(3, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 17', '44', 'pd3.png'),
(4, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 16', '44', 'pd4.png'),
(5, 'NO GAME NO LIFE DESU! เล่มที่ 1', 'สินค้าหมด', 'pd5.png'),
(6, 'NO GAME NO LIFE DESU! เล่มที่ 2', 'สินค้าหมด', 'pd6.png'),
(7, 'NO GAME NO LIFE DESU! เล่มที่ 3', 'สินค้าหมด', 'pd7.png'),
(8, 'NO GAME NO LIFE DESU! เล่มที่ 4', 'สินค้าหมด', 'pd8.png');

-- --------------------------------------------------------

--
-- Table structure for table `user_signin_signup`
--

CREATE TABLE `user_signin_signup` (
  `id` int(11) NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(70) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user_signin_signup`
--

INSERT INTO `user_signin_signup` (`id`, `email`, `username`, `pwd`) VALUES
(1, 'test1@gmail.com', 'test1', 'pbkdf2:sha256:260000$OtlFwW43yQJhBfAc$dce03bbc53b3b8d86050922d62f7fb5af9315b9663ff0f3f078a0f1e984cb503');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_bestseller`
--
ALTER TABLE `product_bestseller`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `product_index`
--
ALTER TABLE `product_index`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `product_promotions`
--
ALTER TABLE `product_promotions`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `user_signin_signup`
--
ALTER TABLE `user_signin_signup`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_bestseller`
--
ALTER TABLE `product_bestseller`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `product_index`
--
ALTER TABLE `product_index`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `product_promotions`
--
ALTER TABLE `product_promotions`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `user_signin_signup`
--
ALTER TABLE `user_signin_signup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

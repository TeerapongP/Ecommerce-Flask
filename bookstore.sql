-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 07, 2022 at 09:58 AM
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

-- --------------------------------------------------------

--
-- Table structure for table `out_of_stock`
--

CREATE TABLE `out_of_stock` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_images` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `out_of_stock`
--

INSERT INTO `out_of_stock` (`product_id`, `product_name`, `product_price`, `product_images`) VALUES
(1, 'NO GAME NO LIFE DESU! เล่มที่ 1', 'สินค้าหมด', 'pd1.png'),
(2, 'NO GAME NO LIFE DESU! เล่มที่ 2', 'สินค้าหมด', 'pd2.png'),
(3, 'NO GAME NO LIFE DESU! เล่มที่ 3', 'สินค้าหมด', 'pd3.png'),
(4, 'NO GAME NO LIFE DESU! เล่มที่ 4', 'สินค้าหมด', 'pd4.png');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_price` int(10) NOT NULL,
  `product_images` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `product_price`, `product_images`) VALUES
(1, 'สารภาพรักกับคุณคางุยะซ ะดีๆ เล่มที่ 21', 55, 'pd1.png'),
(2, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 10', 55, 'pd2.png'),
(3, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 19', 55, 'pd3.png'),
(4, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 20', 55, 'pd4.png'),
(5, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 9', 55, 'pd5.png'),
(6, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 18', 55, 'pd6.png'),
(7, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 19', 55, 'pd7.png'),
(8, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 18', 55, 'pd8.png'),
(9, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 17', 55, 'pd9.png'),
(10, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 16', 55, 'pd10.png'),
(11, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 8', 55, 'pd11.png'),
(12, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 7', 55, 'pd12.png'),
(13, 'มิเอรุโกะจัง ใครว่าหนูเห็นผี เล่มที่ 1', 129, 'pd13.png'),
(14, 'มิเอรุโกะจัง ใครว่าหนูเห็นผี เล่มที่ 2', 129, 'pd14.png'),
(15, 'มิเอรุโกะจัง ใครว่าหนูเห็นผี เล่มที่ 3', 129, 'pd15.png'),
(16, 'มิเอรุโกะจัง ใครว่าหนูเห็นผี เล่มที่ 4', 129, 'pd16.png'),
(17, 'NO GAME NO LIFE เล่มที่ 1', 100, 'pd17.png'),
(18, 'NO GAME NO LIFE เล่มที่ 2', 100, 'pd18.png'),
(19, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 21', 55, 'pd19.png'),
(20, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 20', 55, 'pd20.png'),
(21, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 19', 55, 'pd21.png'),
(22, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 18', 55, 'pd22.png'),
(23, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 19', 55, 'pd23.png'),
(24, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 18', 55, 'pd24.png'),
(25, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 17', 55, 'pd25.png'),
(26, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 16', 55, 'pd26.png'),
(27, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 10', 55, 'pd27.png'),
(28, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 9', 55, 'pd28.png'),
(29, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 8', 55, 'pd29.png'),
(30, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 7', 55, 'pd30.png'),
(31, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 21', 55, 'pd31.png'),
(32, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 20', 55, 'pd32.png'),
(33, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 19', 55, 'pd33.png'),
(34, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 18', 55, 'pd34.png'),
(35, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 10', 55, 'pd35.png'),
(36, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 9', 55, 'pd36.png'),
(37, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 19', 55, 'pd37.png'),
(38, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 18', 55, 'pd38.png'),
(39, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 17', 55, 'pd39.png'),
(40, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 16', 55, 'pd40.png'),
(41, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 8', 55, 'pd41.png'),
(42, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 7', 55, 'pd42.png'),
(43, 'ยากแท้จริงหนอรักของโอตาคุ เล่มที่ 6', 44, 'pd43.png'),
(44, 'เกิดใหม่ทั้งทีก็เป็นสไลม์ไปซะแล้ว เล่มที่ 15', 44, 'pd44.png'),
(45, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 17', 44, 'pd45.png'),
(46, 'สารภาพรักกับคุณคางุยะซะดีๆ เล่มที่ 16', 44, 'pd46.png'),
(47, 'NO GAME NO LIFE DESU! เล่มที่ 1', 0, 'pd47.png'),
(48, 'NO GAME NO LIFE DESU! เล่มที่ 2', 0, 'pd48.png'),
(49, 'NO GAME NO LIFE DESU! เล่มที่ 3', 0, 'pd49.png'),
(50, 'NO GAME NO LIFE DESU! เล่มที่ 4', 0, 'pd50.png');

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
(1, 'test1@gmail.com', 'test1', 'pbkdf2:sha256:260000$OtlFwW43yQJhBfAc$dce03bbc53b3b8d86050922d62f7fb5af9315b9663ff0f3f078a0f1e984cb503'),
(2, 'thirapong.p@ku.th', 'nonrapak707', 'pbkdf2:sha256:260000$Cwouis0lmkG9PsFv$09652fbc7ebfb3b13d21ec3bf2c6b294424adc7b5bc39911cd9c06b5381539e7');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `out_of_stock`
--
ALTER TABLE `out_of_stock`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
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
-- AUTO_INCREMENT for table `out_of_stock`
--
ALTER TABLE `out_of_stock`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `user_signin_signup`
--
ALTER TABLE `user_signin_signup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

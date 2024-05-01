-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2024 at 04:54 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ricetrackerdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `rice_records`
--

CREATE TABLE `rice_records` (
  `id` int(11) NOT NULL,
  `rice_type` varchar(50) DEFAULT NULL,
  `date_planted` date DEFAULT NULL,
  `estimated_date_harvest` date DEFAULT NULL,
  `harvested_rice` int(11) DEFAULT NULL,
  `sacks_sold` int(11) DEFAULT NULL,
  `stocks` int(11) DEFAULT NULL,
  `sales` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rice_records`
--

INSERT INTO `rice_records` (`id`, `rice_type`, `date_planted`, `estimated_date_harvest`, `harvested_rice`, `sacks_sold`, `stocks`, `sales`) VALUES
(1, 'White', '2024-04-30', '2024-08-28', 100, 0, 100, 0),
(2, 'White', '2024-04-30', '2024-08-28', 100, 0, 100, 0),
(3, 'White', '2024-04-30', '2024-08-28', 100, 0, 100, 0),
(4, 'Blue', '2024-04-30', '2024-08-28', 900, 0, 900, 0),
(5, 'Blue', '2024-04-30', '2024-08-28', 900, 0, 900, 0),
(6, 'Blue', '2024-04-30', '2024-08-28', 900, 0, 900, 0),
(7, 'Blue', '2024-04-30', '2024-08-28', 900, 0, 900, 0),
(8, 'Blue', '2024-04-30', '2024-08-28', 900, 0, 900, 0),
(9, 'Blue', '2024-04-30', '2024-08-28', 900, 0, 900, 0),
(10, 'Blue', '2024-04-30', '2024-08-28', 900, 0, 900, 0),
(11, 'Red', '2024-02-21', '2024-06-20', 700, 0, 700, 0),
(12, 'White', '2024-04-30', '2024-08-28', 700, 0, 700, 0),
(13, 'White', '2024-04-30', '2024-08-28', 400, 0, 400, 0),
(14, 'White', '2024-04-30', '2024-08-28', 100, 0, 100, 0),
(15, 'Blue', '2024-04-30', '2024-08-28', 100, 0, 100, 0),
(16, 'Blue', '2024-04-30', '2024-08-28', 500, 0, 500, 0),
(17, 'Blue', '2024-04-30', '2024-08-28', 800, 0, 800, 0),
(18, 'Red', '2024-04-30', '2024-08-28', 800, 0, 800, 0),
(19, 'White', '2024-05-01', '2024-08-29', 100, 0, 100, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rice_records`
--
ALTER TABLE `rice_records`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rice_records`
--
ALTER TABLE `rice_records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

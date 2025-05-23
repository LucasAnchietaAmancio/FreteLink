CREATE TABLE `licenca_validada` (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_validacao` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

CREATE TABLE `motoristas` (
  `id_motorista` int NOT NULL AUTO_INCREMENT,
  `rntrc` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nome` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cpf` varchar(14) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  PRIMARY KEY (`id_motorista`),
  UNIQUE KEY `rntrc` (`rntrc`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

CREATE TABLE `notas` (
  `id_note` int NOT NULL AUTO_INCREMENT,
  `data_emissao` date NOT NULL,
  `data_consulta` date NOT NULL,
  `numero_nota` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `codigo_motorista` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remetente` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `destinatario` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `motorista_id` int DEFAULT NULL,
  PRIMARY KEY (`id_note`),
  KEY `motorista_id` (`motorista_id`),
  CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`motorista_id`) REFERENCES `motoristas` (`id_motorista`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

CREATE TABLE `serialcode` (
  `id` int NOT NULL AUTO_INCREMENT,
  `serial_validacao` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` enum('ativo','inativo') COLLATE utf8mb4_unicode_ci DEFAULT 'ativo',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci


CREATE TRIGGER vincula_serial_motorista_ao_documento
BEFORE INSERT ON notas
FOR EACH ROW
    SET id_motorista = (SELECT id_motorista FROM motorista WHERE rntrc = NEW.codigo_motorista);
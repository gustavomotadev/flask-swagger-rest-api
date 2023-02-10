PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Estilo" (
    "Id"	INTEGER NOT NULL UNIQUE,
    "Nome"	TEXT NOT NULL UNIQUE,
    PRIMARY KEY("Id" AUTOINCREMENT)
);
INSERT INTO Estilo VALUES(1,'Op Art');
INSERT INTO Estilo VALUES(2,'Futurismo');
INSERT INTO Estilo VALUES(3,'Precisionismo');
INSERT INTO Estilo VALUES(4,'Cubismo');
INSERT INTO Estilo VALUES(5,'Expressionismo');
INSERT INTO Estilo VALUES(6,'Impressionismo');
CREATE TABLE IF NOT EXISTS "Autor" (
    "Id"	INTEGER NOT NULL UNIQUE,
    "Nome"	TEXT NOT NULL UNIQUE,
    "AnoNascimento"	INTEGER NOT NULL,
    "AnoFalecimento"	INTEGER,
    "PaisOrigem"	TEXT NOT NULL,
    "UrlImagem"	TEXT NOT NULL,
    PRIMARY KEY("Id" AUTOINCREMENT)
);
INSERT INTO Autor VALUES(1,'Jacob Wexler',1912,1995,'Israel','https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Jacob_Wexler._1978.jpg/609px-Jacob_Wexler._1978.jpg');
INSERT INTO Autor VALUES(2,'Henrique Matos',1961,NULL,'Portugal','https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Henrique_Matos_by_Daniela_Matos_02.jpg/320px-Henrique_Matos_by_Daniela_Matos_02.jpg');
INSERT INTO Autor VALUES(3,'Joseph Stella',1877,1946,'Itália','https://upload.wikimedia.org/wikipedia/en/b/bb/Joseph_Stella.jpg');
INSERT INTO Autor VALUES(4,'Natalia Goncharova',1881,1962,'Rússia','https://upload.wikimedia.org/wikipedia/commons/7/73/Natalia_Sergeyevna_Goncharova.jpg');
INSERT INTO Autor VALUES(5,'Umberto Boccioni',1882,1916,'Itália','https://upload.wikimedia.org/wikipedia/commons/b/ba/Umberto_Boccioni%2C_portrait_photograph.jpg');
INSERT INTO Autor VALUES(6,'John Storrs',1885,1956,'EUA','https://upload.wikimedia.org/wikipedia/en/9/9b/John-Storrs-AAA.jpg');
INSERT INTO Autor VALUES(7,'Charles Demuth',1883,1935,'EUA','https://upload.wikimedia.org/wikipedia/commons/b/be/Charles_Demuth-_Self-Portrait%2C_1907.jpg');
INSERT INTO Autor VALUES(8,'Hennie Niemann',1972,NULL,'África do Sul','https://hennieniemannjnr.com/wp-content/uploads/2020/09/About-Me-2-1024x683.jpg');
INSERT INTO Autor VALUES(9,'Tadeusz Makowski',1882,1932,'Polônia','https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/TadeuszMakowski.AutoportretZPaletaIPtaszkiem.1919.ws.jpg/459px-TadeuszMakowski.AutoportretZPaletaIPtaszkiem.1919.ws.jpg');
INSERT INTO Autor VALUES(10,'Fritz Stuckenberg',1881,1944,'Alemanha','https://upload.wikimedia.org/wikipedia/commons/7/72/Fritz_Stuckenberg_Selbstbildnis_1915.jpg');
INSERT INTO Autor VALUES(11,'Domḗnikos Theotokópoulos',1541,1614,'Ducado de Cândia (Atual Grécia)','https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/El_Greco_-_Portrait_of_a_Man_-_WGA10554.jpg/433px-El_Greco_-_Portrait_of_a_Man_-_WGA10554.jpg');
INSERT INTO Autor VALUES(12,'Wassily Kadinsky',1866,1944,'Império Russo','https://upload.wikimedia.org/wikipedia/commons/8/8a/Vassily-Kandinsky.jpeg');
INSERT INTO Autor VALUES(13,'Edvard Munch',1863,1944,'Noruega','https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Portrett_av_Edvard_Munch_%28cropped%29.jpg/397px-Portrett_av_Edvard_Munch_%28cropped%29.jpg');
INSERT INTO Autor VALUES(14,'Walter Gramatté',1897,1929,'Alemanha','https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Walter_Gramatt%C3%A9_%281929%29%2C_by_Minya_Diez-D%C3%BChrkoop.jpg/354px-Walter_Gramatt%C3%A9_%281929%29%2C_by_Minya_Diez-D%C3%BChrkoop.jpg');
INSERT INTO Autor VALUES(15,'Pierre-Auguste Renoir',1841,1919,'França','https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Pierre_Auguste_Renoir%2C_uncropped_image.jpg/484px-Pierre_Auguste_Renoir%2C_uncropped_image.jpg');
INSERT INTO Autor VALUES(16,'Camille Pissarro',1830,1903,'Ilhas Virgens','https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Pissarro-portrait.jpg/449px-Pissarro-portrait.jpg');
INSERT INTO Autor VALUES(17,'Édouard Manet',1832,1883,'França','https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/%C3%89douard_Manet%2C_en_buste%2C_de_face_-_Nadar.jpg/361px-%C3%89douard_Manet%2C_en_buste%2C_de_face_-_Nadar.jpg');
INSERT INTO Autor VALUES(18,'Claude Monet',1840,1926,'França','https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Claude_Monet_1899_Nadar_crop.jpg/360px-Claude_Monet_1899_Nadar_crop.jpg');
CREATE TABLE IF NOT EXISTS "Obra" (
    "Id"	INTEGER NOT NULL UNIQUE,
    "Titulo"	TEXT NOT NULL,
    "Autor"	INTEGER NOT NULL,
    "Ano"	INTEGER NOT NULL,
    "Estilo"	INTEGER NOT NULL,
    "Material"	BLOB NOT NULL,
    "UrlImagem"	TEXT NOT NULL,
    FOREIGN KEY("Autor") REFERENCES "Autor"("Id") ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY("Estilo") REFERENCES "Estilo"("Id") ON UPDATE CASCADE ON DELETE RESTRICT,
    PRIMARY KEY("Id" AUTOINCREMENT)
);
INSERT INTO Obra VALUES(1,'Construction on Red Background',1,1968,1,'Acrílico sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/1968_Construction_on_Red_Background.jpg/671px-1968_Construction_on_Red_Background.jpg');
INSERT INTO Obra VALUES(2,'Torso',1,1968,1,'Acrílico sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/1968_Torso.jpg/768px-1968_Torso.jpg');
INSERT INTO Obra VALUES(3,'The Second Day',1,1974,1,'Acrílico sobre painel','https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/1974_The_Second_Day.jpg/768px-1974_The_Second_Day.jpg');
INSERT INTO Obra VALUES(4,'Movimento óptico III',2,2012,1,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/2/27/2012_Henrique_Matos_Optical_Motion_III_02.jpg');
INSERT INTO Obra VALUES(5,'Viagem ao infinito',2,2006,1,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Henrique_Matos_2006_Viagem_ao_infinito_01.jpg/1024px-Henrique_Matos_2006_Viagem_ao_infinito_01.jpg');
INSERT INTO Obra VALUES(6,'Battle of Lights, Coney Island, Mardi Gras',3,1914,2,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Joseph_Stella%2C_1913%E2%80%9314%2C_Battle_of_Lights%2C_Coney_Island%2C_Mardi_Gras%2C_oil_on_canvas%2C_195.6_%C3%97_215.3_cm%2C_Yale_University_Art_Gallery.tif/lossy-page1-851px-Joseph_Stella%2C_1913%E2%80%9314%2C_Battle_of_Lights%2C_Coney_Island%2C_Mardi_Gras%2C_oil_on_canvas%2C_195.6_%C3%97_215.3_cm%2C_Yale_University_Art_Gallery.tif.jpg');
INSERT INTO Obra VALUES(7,'Cyclist',4,1913,2,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Cyclist_%28Goncharova%2C_1913%29.jpg/639px-Cyclist_%28Goncharova%2C_1913%29.jpg');
INSERT INTO Obra VALUES(8,'Elasticity',5,1912,2,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Umberto_Boccioni%2C_1912%2C_Elasticity_(Elasticit%C3%A0)%2C_oil_on_canvas%2C_100_x_100_cm%2C_Museo_del_Novecento.jpg/776px-Umberto_Boccioni%2C_1912%2C_Elasticity_(Elasticit%C3%A0)%2C_oil_on_canvas%2C_100_x_100_cm%2C_Museo_del_Novecento.jpg');
INSERT INTO Obra VALUES(9,'Brooklyn Bridge',3,1920,3,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Joseph_Stella%2C_1919-20%2C_Brooklyn_Bridge%2C_oil_on_canvas%2C_215.3_x_194.6_cm%2C_Yale_University_Art_Gallery.jpg/694px-Joseph_Stella%2C_1919-20%2C_Brooklyn_Bridge%2C_oil_on_canvas%2C_215.3_x_194.6_cm%2C_Yale_University_Art_Gallery.jpg');
INSERT INTO Obra VALUES(10,'Profile Head with Cap',6,1918,3,'Xilogravura em papel','https://upload.wikimedia.org/wikipedia/commons/b/b3/Head_Woodcut_1920.jpg');
INSERT INTO Obra VALUES(11,'Chimney and Water Tower',7,1931,3,'Óleo sobre madeira','https://upload.wikimedia.org/wikipedia/commons/a/a2/Demuth_Charles_Chimney_and_Watertower_1931.jpg');
INSERT INTO Obra VALUES(12,'The Visitor',8,2019,4,'Óleo sobre linho','https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/%27The_Visitor%27%2C_120x100cm%2C_Oil_on_Belgian_linen_by_Hennie_Niemann_jnr_signed_and_dated_lower_left%2C_2019.jpg/899px-%27The_Visitor%27%2C_120x100cm%2C_Oil_on_Belgian_linen_by_Hennie_Niemann_jnr_signed_and_dated_lower_left%2C_2019.jpg');
INSERT INTO Obra VALUES(13,'Woman with buckets',9,1913,4,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/3/32/Makowski_Woman_with_buckets.jpg');
INSERT INTO Obra VALUES(14,'The Lovers. Portrait of Paul and Emmeke van Ostaijen',10,1919,4,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Fritz_Stuckenberg_Das_Liebespaar.jpeg/595px-Fritz_Stuckenberg_Das_Liebespaar.jpeg');
INSERT INTO Obra VALUES(15,'View of Toledo',11,1600,5,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/El_Greco_View_of_Toledo.jpg/680px-El_Greco_View_of_Toledo.jpg');
INSERT INTO Obra VALUES(16,'The Blue Rider',12,1903,5,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Wassily_Kandinsky%2C_1903%2C_The_Blue_Rider_%28Der_Blaue_Reiter%29%2C_oil_on_canvas%2C_52.1_x_54.6_cm%2C_Stiftung_Sammlung_E.G._B%C3%BChrle%2C_Zurich.jpg/800px-Wassily_Kandinsky%2C_1903%2C_The_Blue_Rider_%28Der_Blaue_Reiter%29%2C_oil_on_canvas%2C_52.1_x_54.6_cm%2C_Stiftung_Sammlung_E.G._B%C3%BChrle%2C_Zurich.jpg');
INSERT INTO Obra VALUES(17,'The scream of nature',13,1893,5,'Têmpera e giz de cera sobre madeira','https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg/619px-Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg');
INSERT INTO Obra VALUES(18,'Storm',14,1915,5,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/B.3_Sturm._Storm._1915.jpg/912px-B.3_Sturm._Storm._1915.jpg');
INSERT INTO Obra VALUES(19,'Dance at Le moulin de la Galette',15,1876,6,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Pierre-Auguste_Renoir%2C_Le_Moulin_de_la_Galette.jpg/1024px-Pierre-Auguste_Renoir%2C_Le_Moulin_de_la_Galette.jpg');
INSERT INTO Obra VALUES(20,'On the Terrasse',15,1881,6,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Two_Sisters_%28On_the_Terrace%29.jpg/625px-Two_Sisters_%28On_the_Terrace%29.jpg');
INSERT INTO Obra VALUES(21,'Hay Harvest at Éragny',16,1901,6,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Hay_Harvest_at_%C3%89ragny%2C_1901%2C_Camille_Pissarro.jpg/920px-Hay_Harvest_at_%C3%89ragny%2C_1901%2C_Camille_Pissarro.jpg');
INSERT INTO Obra VALUES(22,'A Bar at the Folies-Bergère',17,1882,6,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Edouard_Manet%2C_A_Bar_at_the_Folies-Berg%C3%A8re.jpg/1024px-Edouard_Manet%2C_A_Bar_at_the_Folies-Berg%C3%A8re.jpg');
INSERT INTO Obra VALUES(23,'Jerusalem Artichoke Flowers',18,1880,6,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Jerusalem_Artichoke_Flowers_E10330.jpg/556px-Jerusalem_Artichoke_Flowers_E10330.jpg');
INSERT INTO Obra VALUES(24,'Woman with a Parasol - Madame Monet and Her Son',18,1875,6,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Claude_Monet_-_Woman_with_a_Parasol_-_Madame_Monet_and_Her_Son_-_Google_Art_Project.jpg/618px-Claude_Monet_-_Woman_with_a_Parasol_-_Madame_Monet_and_Her_Son_-_Google_Art_Project.jpg');
INSERT INTO Obra VALUES(25,'Garden at Sainte-Adresse',18,1867,6,'Óleo sobre tela','https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Claude_Monet_-_Jardin_%C3%A0_Sainte-Adresse.jpg/1024px-Claude_Monet_-_Jardin_%C3%A0_Sainte-Adresse.jpg');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('Estilo',6);
INSERT INTO sqlite_sequence VALUES('Autor',18);
INSERT INTO sqlite_sequence VALUES('Obra',25);
COMMIT;
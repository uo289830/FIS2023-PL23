drop table if exists Atletas;
drop table if exists Actividades;
drop table if exists Subtipos;
drop table if exists Objetivos;
drop table if exists ActividadEntidades;
drop table if exists Inscripciones;

create table Atletas (correo_electronico varchar(100) unique not null primary key, nombre varchar(32), apellidos varchar(32),fecha_alta varchar(10),
                            fecha_nacimiento varchar(10),peso varchar(10),Altura varchar(10), tipo_atleta varchar(32),IBAN varchar(64),
                            Numero_tarjeta varchar (32),fecha_caducidad varchar(10),CVV varchar(10));
create table Actividades (idactividad INTEGER primary key,nombre_actividad varchar(32) not null, nombre_subtipo varchar(100) not null,  fecha varchar(10),
                       duracion float, localizacion varchar(32), distancia float , FCmax int, FCmin int,
                       correo_electronico varchar(100) not null,
                       foreign key (correo_electronico) references Atletas (correo_electronico));
create table Subtipos (nombre_subtipo varchar(100) not null , met float );

create table Objetivos (idobjetivo integer primary key AUTOINCREMENT, correo_electronico varchar(100) not null, tipo_objetivo varchar(32) not null, valor_objetivo int not null,
                            foreign key (correo_electronico) references Atletas (correo_electronico));

create table ActividadEntidades (idactividadentidad INTEGER primary key, nombre_entidad varchar(100) , nombre_activ_entidad varchar(100) ,descripcion varchar(300),fecha varchar(10),duracion_dias int,hora_inicio varchar(5),lugar varchar(100),plazas int,coste_UsFree float,info_adicional varchar(300));

create table Inscripciones (idinscripcion INTEGER primary key,correo_electronico varchar(100),idactividadentidad INTEGER, foreign key (correo_electronico) references Atletas (correo_electronico),foreign key (idactividadentidad) references ActividadEntidades (idactividadentidad));
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Provinsi(Base):
    __tablename__ = "wilayah"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    singkatan_umum = Column(String)
    singkatan_iso = Column(String)
    kode_wilayah = Column(String)
    wilayah_geografis = Column(String)
    ibu_kota = Column(String)
    gubernur = Column(String)
    hari_jadi = Column(String)
    populasi = Column(String)
    luas = Column(String)
    kepadatan_penduduk = Column(String)
    ipm_bps = Column(String)
    apbd_pendapatan = Column(String)
    apbd_belanja = Column(String)
    prdb_total = Column(String)
    prdb_perkapita = Column(String)

    kabupatens = relationship("Kabupaten", back_populates="wilayah")

class Kabupaten(Base):
    __tablename__ = "kabupatens"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    provinsi_id = Column(Integer, ForeignKey("wilayah.id"))

    wilayah = relationship("Provinsi", back_populates="kabupatens")
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

class ProvinsiBase(BaseModel):
    name: str
    singkatan_umum: str
    singkatan_iso: str
    kode_wilayah: str
    wilayah_geografis: str
    ibu_kota: str
    gubernur: str
    hari_jadi: str
    populasi: str
    luas: str
    kepadatan_penduduk: str
    ipm_bps: str
    apbd_pendapatan: str
    apbd_belanja: str
    prdb_total: str
    prdb_perkapita: str

class Provinsi(ProvinsiBase):
    id: int

    class Config:
        orm_mode = True

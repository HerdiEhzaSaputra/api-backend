from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


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
    name: str | None = None
    singkatan_umum: str | None = None
    singkatan_iso: str | None = None
    kode_wilayah: str | None = None
    wilayah_geografis: str | None = None
    ibu_kota: str | None = None
    gubernur: str | None = None
    hari_jadi: str | None = None
    populasi: str | None = None
    luas: str | None = None
    kepadatan_penduduk: str | None = None
    ipm_bps: str | None = None
    apbd_pendapatan: str | None = None
    apbd_belanja: str | None = None
    prdb_total: str | None = None
    prdb_perkapita: str | None = None

class Provinsi(ProvinsiBase):
    id: int

    class Config:
        orm_mode = True

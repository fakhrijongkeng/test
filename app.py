from prefect import flow, task

@task
def ambil_data():
    return "Data mentah dari lokal"

@task
def proses_data(data):
    return f"{data} sudah dibersihkan!"

@flow(log_prints=True)
def flow_belajar_prefect():
    print("Memulai alur kerja...")
    mentah = ambil_data()
    hasil = proses_data(mentah)
    print(hasil)

if __name__ == "__main__":
    flow_belajar_prefect()
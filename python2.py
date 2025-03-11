{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Elenanda/Repo_ML/blob/main/python2\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6gY6aflt_l6c"
      },
      "source": [
        "# Python Basic 2\n",
        "Boolean values, conditional execution, loops, lists and list processing, logical and bitwise operationsExternal tool\n",
        "\n",
        "Referensi Tambahan:\n",
        "- https://docs.python.org/3.8/\n",
        "- https://docs.python.org/id/3.8/tutorial/\n",
        "\n",
        "\n",
        "## Materi\n",
        "\n",
        "- Operator relasional;\n",
        "- Operator aritmatika;\n",
        "- Struktur pemilihan if-elif-else;\n",
        "- Struktur perulangan while dan for;\n",
        "- Statement loncat;\n",
        "- Operasi logika dan bitwise;\n",
        "- Lists dan Array."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Rx7ralgf_l6e"
      },
      "source": [
        "#### Mutable dan Immutable\n",
        "Mutable : List, Dictionary\n",
        "\n",
        "Immutable : String, Bilangan dan Tuple"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sWnVsS7W_l6f",
        "outputId": "9ea0087d-d803-4d79-dbd6-c062bb9251a0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n",
            "10751464\n"
          ]
        }
      ],
      "source": [
        "a=20\n",
        "print(a)\n",
        "print(id(a))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KFpHy3ht_l6g",
        "outputId": "ba98c108-f744-4925-a2bd-22562de6d627"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n",
            "10751784\n"
          ]
        }
      ],
      "source": [
        "a=30\n",
        "print(a)\n",
        "print(id(a))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ov_CidQ-_l6g",
        "outputId": "bbb88d35-1bfd-4c9e-f6e3-b5241fd8b1eb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4]\n",
            "<class 'list'>\n",
            "134209129282496\n"
          ]
        }
      ],
      "source": [
        "a=[1,2,3,4]\n",
        "print(a)\n",
        "print(type(a))\n",
        "print(id(a))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hcgVGwXX_l6g",
        "outputId": "1741da28-a97a-4d26-81c0-e6be723154d0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 2, 3, 4]\n",
            "134209129282496\n"
          ]
        }
      ],
      "source": [
        "a[0]=0\n",
        "print(a)\n",
        "print(id(a))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HRz57MOx_l6h"
      },
      "source": [
        "## Operator Relasional\n",
        "Operator relasional adalah operator yang digunakan untuk membandingkan dua buah nilai. Hasil yang akan diperoleh dari operasi perbandingan ini adalah logika (bertipe bool), yaitu True (benar) atau False (salah).\n",
        "\n",
        "![operator%20relasional.png](attachment:operator%20relasional.png)\n",
        "\n",
        "### Prioritas Operator\n",
        "| Prioritas| Operator |        |\n",
        "|----------|----------|--------|\n",
        "| 1        | +, -     | unary  |\n",
        "| 2        | **       |        |\n",
        "| 3        | *,/,//,% |        |\n",
        "| 4        | +, -     | binary |"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XeMPz2Cg_l6h"
      },
      "source": [
        "## Latihan: Questions and answers\n",
        "\n",
        "Gunakan operator relasional untuk mendeteksi nilai integer < 100 atau >= 100\n",
        "\n",
        "#### Test Data\n",
        "\n",
        "Sample input: 55\n",
        "\n",
        "`Expected output: False`\n",
        "\n",
        "Sample input: 99\n",
        "\n",
        "`Expected output: False`\n",
        "\n",
        "Sample input: 100\n",
        "\n",
        "`Expected output: True`\n",
        "\n",
        "Sample input: 101\n",
        "\n",
        "`Expected output: True`\n",
        "\n",
        "Sample input: -5\n",
        "\n",
        "`Expected output: False`\n",
        "\n",
        "Sample input: +123\n",
        "\n",
        "`Expected output: True`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6W9sHJvm_l6h",
        "outputId": "62963c03-79dc-493e-800a-af71b8a5e99a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sample input: 101\n",
            "Expected output:  True\n"
          ]
        }
      ],
      "source": [
        "a=int(input(\"Sample input: \"))\n",
        "print(\"Expected output: \", a>=100)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "w9dFueAN_l6h"
      },
      "source": [
        "# Operator Aritmatika\n",
        "\n",
        "Operator aritmatika adalah operator yang digunakan untuk melakukan perhitungan terhadap data numerik. Berikut merupakan operator aritmatika yang digunakan dalam python :\n",
        "\n",
        "![operator%20aritmatika.JPG](attachment:operator%20aritmatika.JPG)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hYjfghKi_l6i"
      },
      "source": [
        "</b> Prioritas operator </b>\n",
        "Setiap operator aritmatika memiliki prioritas yang berbeda. Sebagai contoh :\n",
        "\n",
        "</b> 3+5*7 </b>\n",
        "Seperti yang diketahui, operator perkalian (*) memiliki prioritas yang lebih tinggi dibandingkan dengan operator penjumlahan (+) sehingga operasi dapat dituliskan sebagai berikut (3+(5*7)).\n",
        "\n",
        "Untuk lebih jelasnya, tabel berikut memperlihatkan urutan prioritas dari operator aritmatika :\n",
        "![prioritas.JPG](attachment:prioritas.JPG)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "02l8LHq4_l6i"
      },
      "source": [
        "Berikut merupakan mindmap dari operasi aritmatika :\n",
        "\n",
        "![mindmad%20aritmatika.JPG](attachment:mindmad%20aritmatika.JPG)\n",
        "\n",
        "Perhatikan contoh dibawah :\n",
        "\n",
        "x = 5 + 2 * 3 / (2 - 3) ** 2\n",
        "berapa nilai x?\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ftb7WWnu_l6i",
        "outputId": "02675df1-b115-42be-f4fb-d6995c6c1d67"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11.0\n"
          ]
        }
      ],
      "source": [
        "x = 5 + 2 * 3 / (2 - 3) ** 2\n",
        "print(x)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ji2WVzSb_l6i"
      },
      "source": [
        "## Struktur Pemilihan\n",
        "\n",
        "Berbeda dengan bahasa pemrograman lainnya, Python hanya memiliki satu statement untuk melakukan proses pemilihan, yaitu dengan menggunakan if. Untuk mempermudah pembahasan tentang statement if, pembahasan akan dibagi menjadi tiga kelompok :\n",
        "\n",
        " - Statement if untuk satu kasus\n",
        " - Statement if untuk dua kasus\n",
        " - Statement if untuk tiga kasus"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VS3nKDM8_l6j"
      },
      "source": [
        "### 1. Statement if untuk satu kasus\n",
        "\n",
        "Bentuk umum penggunaan perintah if untuk satu kasus dalam Python adalah :\n",
        "\n",
        "```python\n",
        "if kondisi:\n",
        "    statement1\n",
        "    statement2\n",
        "    ...\n",
        "    \n",
        "```\n",
        "Pada bentuk diatas, statement1, statement2 dan seterusnya hanya akan dieksekusi jika kondisi yang didefinisikan dalam perintah If terpenuhi (bernilai True). Jika kondisi bernilai False, statement tersebut akan diabaikan oleh program.\n",
        "\n",
        "Perhatikan contoh berikut :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "M4u3r-Yj_l6j"
      },
      "outputs": [],
      "source": [
        "a = 5\n",
        "b = 6\n",
        "\n",
        "if a==b:\n",
        "    print(\"oke\")\n",
        "    print(\"berhasil\")\n",
        "    print(\"Gagal\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jFcV1Utp_l6j"
      },
      "source": [
        "### 2. Statement if untuk dua kasus\n",
        "\n",
        "Untuk pemilihan yang mengandung dua kasus, bentuk umum yang digunakan adalah :\n",
        "\n",
        "```python\n",
        "if kondisi :\n",
        "    statement1\n",
        "    statement2\n",
        "    ...\n",
        "else\n",
        "    statement_alternatif1\n",
        "    statement_alternatif2\n",
        "    ...\n",
        "```\n",
        "\n",
        "Pada bentuk ini, jika kondisi bernilai True makan statement selanjutnya yang akan dieksekusi oleh program adalah statement1, stetement 2 dan seterusnya. Tapi jika kondisi bernilai False, maka program akan mengeksekusi statement yang berada pada bagian else, yaitu statement_alternatif1, statement_alternatif2 dan seterusnya."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zSb73pT__l6j",
        "outputId": "70cf999f-481e-4ab9-ca9a-f51de1e8542d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Gagal\n"
          ]
        }
      ],
      "source": [
        "a = 5\n",
        "b = 6\n",
        "\n",
        "if a==b:\n",
        "    print(\"oke\")\n",
        "    print(\"berhasil\")\n",
        "else:\n",
        "    print(\"Gagal\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dx70pzER_l6k"
      },
      "source": [
        "#### Latihan 1\n",
        "Memasukan bilangan bulat dan mendeteksi bilangan tersebut genap / ganjil."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CJRZJmhl_l6k",
        "outputId": "ea958855-9536-4c34-d3a9-4d85de5d58b7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukan bilangan bulat: 3\n",
            "ganjil\n"
          ]
        }
      ],
      "source": [
        "bil = int(input(\"Masukan bilangan bulat: \"))\n",
        "\n",
        "if(bil%2 == 0):\n",
        "    print(\"genap\")\n",
        "else:\n",
        "    print(\"ganjil\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZYnK66zt_l6k"
      },
      "source": [
        "### 3. Statement if untuk Tiga kasus atau lebih\n",
        "\n",
        "Struktur pemilihan jenis ini merupakan bentuk yang paling kompleks jika dibandingkan dengan kedua jenis yang sudah di bahas diatas. Dalam struktur ini, ada beberapa kondisi yang harus diperiksa oleh program. Bentuk umum penggunaan perintah if untuk tiga kasus atau lebih adalah :\n",
        "\n",
        "```python\n",
        "if kondisi1:\n",
        "    statement1a\n",
        "    statement1b\n",
        "    ...\n",
        "elif kondisi2:\n",
        "    statement2a\n",
        "    statement2b\n",
        "    ...\n",
        "else:\n",
        "    statement_alternatif1\n",
        "    statement_alternatif2\n",
        "    ...\n",
        "```\n",
        "Perhatikan contoh dibawah ini :"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "79xAXSIH_l6k"
      },
      "source": [
        "#### Latihan 2\n",
        "\n",
        "![kuadran.jpg](attachment:kuadran.jpg)\n",
        "\n",
        "Perhatikan gambar diatas. Penetuan kuadran dari suatu titik dilakukan dengan cara :\n",
        "\n",
        " - Jika x>0 dan y>0 maka titik akan berada pada Kuadran I\n",
        " - Jika x<0 dan y>0 maka titik akan berapa pada Kuadran II\n",
        " - Jika x<0 dan y<0 maka titik akan berada pada Kuadran III\n",
        " - JIka x>0 dan y<0 maka titik akan berada pada Kuadran IV\n",
        " - Jika keepat kondisi ini tidak dapat dipenuhi, maka titik tidak termasuk pada kuadran manapun\n",
        "\n",
        "Tuliskan kondisi tersebut dalam bahasa Python."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "stubGbf__l6l",
        "outputId": "b4d3d87c-718d-4786-aea0-aa30f3d24093"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukan nilai koordinat\n",
            "Nilai x: 4\n",
            "Nilai y: 1\n",
            "Koordinat (4,1) berada pada Kuadran I\n"
          ]
        }
      ],
      "source": [
        "print(\"Masukan nilai koordinat\")\n",
        "x = int(input(\"Nilai x: \"))\n",
        "y = int(input(\"Nilai y: \"))\n",
        "\n",
        "if x>0 and y>0:\n",
        "    print(\"Koordinat (\"+ str(x) + \",\"+ str(y) +\") berada pada Kuadran I\" )\n",
        "elif x<0 and y>0:\n",
        "    print(\"Koordinat (\"+ str(x) + \",\"+ str(y) +\") berada pada Kuadran II\" )\n",
        "elif x<0 and y<0:\n",
        "    print(\"Koordinat (\"+ str(x) + \",\"+ str(y) +\") berada pada Kuadran III\" )\n",
        "elif x>0 and y<0:\n",
        "    print(\"Koordinat (\"+ str(x) + \",\"+ str(y) +\") berada pada Kuadran IV\" )\n",
        "else:\n",
        "    pass"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3f1Zy-BT_l6l"
      },
      "source": [
        "#### Latihan 3\n",
        "Mencari bilangan terbesar, dari 3 inputan (a, b dan c)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mSB28Kuo_l6l",
        "outputId": "1fdbc558-b72b-450b-c66f-9284690ee9c7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First Number : 1\n",
            "Second Number : 5\n",
            "Third Number : 1\n",
            "The largest number is:  5\n"
          ]
        }
      ],
      "source": [
        "num1 = int(input(\"First Number : \"))\n",
        "num2 = int(input(\"Second Number : \"))\n",
        "num3 = int(input(\"Third Number : \"))\n",
        "\n",
        "#set number1 sebagai yang terbesar\n",
        "largestNum = num1\n",
        "\n",
        "#deteksi apakah num2 > num1\n",
        "if num2 > largestNum:\n",
        "    largestNum = num2\n",
        "\n",
        "#deteksi apakah num3 > num2\n",
        "if num3 > largestNum:\n",
        "    largestNum = num3\n",
        "\n",
        "print(\"The largest number is: \", largestNum)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "97YZ7sAk_l6l"
      },
      "source": [
        "## Latihan\n",
        "Spathiphyllum, atau yang sering disebut dengan 'peace lily' atau tanaman 'white sail merupakan tanaman dalam rumah yang sangat populer yang dapat menjadi filter guna menyaring udara dari racun. Beberapa racun yang dapat di filter adalah benzena, fomaldehyde, dan amonia.\n",
        "\n",
        "Bayangkan bahwa program komputer anda sangat menyukai tanaman. Ketika komputer menerima masukan (input) pada form \"Spathiphyllum\", maka komputer akan merespon dengan \"Spathiphyllum is the best plant ever!\".\n",
        "\n",
        "Tulislah sebuah program dengan Python untuk beberapa kondisi berikut, input adalah sebuah string :\n",
        "\n",
        "- respon komputer :  `\"Yes - Spathiphyllum is the best plant ever!\"` ketika input berupa `\"Spathiphyllum\"` (upper-case)\n",
        "- respon komputer :  `\"No, I want a big Spathiphyllum!\"` ketika input berupa `\"spathiphyllum\"` (lower-case)\n",
        "- respon komputer :  `\"Spathiphyllum! Not [input]!\"` ketika input berupa \"input\"."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3X_QhLec_l6l",
        "outputId": "9ebcdc4f-f6d8-49ea-8528-b5481cddfce5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please input a best plant = spathiphyllum\n",
            "No, I want a big Spathiphyllum!\n"
          ]
        }
      ],
      "source": [
        "plant = input(\"Please input a best plant = \")\n",
        "\n",
        "if plant == \"Spathiphyllum\":\n",
        "    print(\"Yes - Spathiphyllum is the best plant ever!\")\n",
        "elif plant == \"spathiphyllum\":\n",
        "    print(\"No, I want a big Spathiphyllum!\")\n",
        "else:\n",
        "    print(\"Spathiphyllum! Not \"+ plant +\"!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zxedJ-xR_l6m"
      },
      "source": [
        "## Latihan\n",
        "\n",
        "\n",
        "Pada suatu masa terdapat sebuah daratan - daratan dengan susu dan madu, yang dihuni oleh masyarakat yang bahagia dan sejahtera. Masyarakat tersebut membayar pajak, sehingga kebahagiaan mereka memiliki batas. Pajak yang paling penting adalah Personal Income Tax atau disebut PIT yang mana harus dibayarkan tiap tahun, dan dievaluasi dengan peraturan sebagai berikut :  \n",
        "\n",
        "- Jika penghasilan tidak lebih besar daripada 85,528 thaler, maka pajak adalah sebesar 18% dari pemasukan dikurangi 556 thaler dan 2 sen (disebut juga tax relief)\n",
        "- Jika penghasilan lebih dari nilai tersebut, maka pajak adalah sebesar 14,839 thaler and 2 cents, ditambah 32% dari selisih penghasilan dengan 85,528 thalers.\n",
        "\n",
        "Tugas anda adalah membuat <b>tax calculator</b>.\n",
        "\n",
        "- Harus menerima satu masukan : penghasilan\n",
        "- Berikutnya, print pajak yang telah dihitung, nilai dibulatkan penuh ke thaler (tanpa sen). Fungsi round() akan membantu anda untuk membulatkan nilai.\n",
        "\n",
        "Catatan : Negara yang bahagia ini tidak pernah mengembalikan uang tersebut ke warganya. Jika perhitungan pajak kurang dari nol, itu berarti warga tidak dikenakan pajak sama sekali (pajak = 0).\n",
        "    \n",
        "Perhatikan syntax dibawah ini, hanya membaca satu input dan output sebagai hasilnya. Lengkapi syntax tersebut dengan sebuah perhitungan yang cerdas.\n",
        "\n",
        "```python\n",
        "income = float(input(\"Enter the annual income: \"))\n",
        "\n",
        "#\n",
        "# Put your code here.\n",
        "#\n",
        "\n",
        "tax = round(tax, 0)\n",
        "print(\"The tax is:\", tax, \"thalers\")\n",
        "```\n",
        "\n",
        "Test your code using the data we've provided.\n",
        "\n",
        "```python\n",
        "Sample input: 10000\n",
        "\n",
        "Expected output: The tax is: 1244.0 thalers\n",
        "        \n",
        "Sample input: 100000\n",
        "\n",
        "Expected output: The tax is: 19470.0 thalers\n",
        "        \n",
        "Sample input: 1000\n",
        "\n",
        "Expected output: The tax is: 0.0 thalers\n",
        "\n",
        "Sample input: -100\n",
        "\n",
        "Expected output: The tax is: 0.0 thalers"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xQ4temAG_l6m",
        "outputId": "521d5c7d-95eb-421e-8d70-3cc03c426b55"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the annual income: 1000\n",
            "The tax is: 0 thalers\n"
          ]
        }
      ],
      "source": [
        "income = float(input(\"Enter the annual income: \"))\n",
        "tax = 0\n",
        "\n",
        "if income<85528:\n",
        "    tax = 0.18 * income - 556.2\n",
        "else:\n",
        "    tax = 14839 + 0.2 + 0.32 * (income - 85528)\n",
        "\n",
        "tax = round(tax, 0)\n",
        "\n",
        "if tax<0:\n",
        "    tax = 0\n",
        "\n",
        "print(\"The tax is:\", tax, \"thalers\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vDUUyhKD_l6m"
      },
      "source": [
        "## Latihan\n",
        "\n",
        "As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.\n",
        "\n",
        "Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:\n",
        "\n",
        "- if the year number isn't divisible by four, it's a common year;\n",
        "- otherwise, if the year number isn't divisible by 100, it's a leap year;\n",
        "- otherwise, if the year number isn't divisible by 400, it's a common year;\n",
        "- otherwise, it's a leap year.\n",
        "\n",
        "Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.\n",
        "\n",
        "``` python\n",
        "year = int(input(\"Enter a year: \"))\n",
        "\n",
        "#\n",
        "# Put your code here.\n",
        "#\n",
        "\n",
        "```\n",
        "\n",
        "The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.\n",
        "\n",
        "It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.\n",
        "\n",
        "Test your code using the data we've provided.\n",
        "\n",
        "Sample input: `2000`\n",
        "\n",
        "Expected output: `Leap year`\n",
        "\n",
        "Sample input: `2015`\n",
        "\n",
        "Expected output: `Common year`\n",
        "\n",
        "Sample input: `1999`\n",
        "\n",
        "Expected output: `Common year`\n",
        "\n",
        "Sample input: `1996`\n",
        "\n",
        "Expected output: `Leap year`\n",
        "\n",
        "Sample input: `1580`\n",
        "\n",
        "Expected output: `Not within the Gregorian calendar period`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y4GwD6xH_l6m",
        "outputId": "6881f721-7ead-4bde-c111-8a59752de236"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a year: 1999\n",
            "common year\n"
          ]
        }
      ],
      "source": [
        "year = int(input(\"Enter a year: \"))\n",
        "\n",
        "if year < 1582:\n",
        "    print(\"Not within the Gregorian calender period\")\n",
        "else :\n",
        "    if year % 4 !=0 :\n",
        "        print(\"common year\")\n",
        "    elif year % 100 !=0:\n",
        "        print (\"leap year\")\n",
        "    elif year % 400 !=0:\n",
        "        print(\"common year\")\n",
        "    else :\n",
        "        print(\"leap year\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qXmNuuTY_l6m"
      },
      "source": [
        "#### Latihan-latihan"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sWePvR3h_l6m"
      },
      "source": [
        "Apakah luaran dari syntax berikut :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qalfxp2n_l6n",
        "outputId": "fa08db8f-491b-440d-9205-7c400d7be656"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n"
          ]
        }
      ],
      "source": [
        "x = 5\n",
        "y = 10\n",
        "z = 8\n",
        "\n",
        "print(x > y)\n",
        "print(y > z)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QSsIcLTr_l6n",
        "outputId": "7d77a755-76a6-457c-ca8a-b103acec0ec4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "True\n"
          ]
        }
      ],
      "source": [
        "x, y, z = 5, 10, 8\n",
        "\n",
        "print(x > z)\n",
        "print((y - 5) == x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rj1ZP-Vn_l6n",
        "outputId": "0ad0bb2d-b756-4e88-e4e9-a1e57a79bc37"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "False\n"
          ]
        }
      ],
      "source": [
        "x, y, z = 5, 10, 8\n",
        "x, y, z = z, y, x\n",
        "\n",
        "print(x > z)\n",
        "print((y - 5) == x)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3NkVey2o_l6n",
        "outputId": "b53f2667-812b-475f-a930-5de28e7020c4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "True\n",
            "else\n"
          ]
        }
      ],
      "source": [
        "x = 10\n",
        "\n",
        "if x == 10:\n",
        "    print(x == 10)\n",
        "\n",
        "if x > 5:\n",
        "    print(x > 5)\n",
        "\n",
        "if x < 10:\n",
        "    print(x < 10)\n",
        "else:\n",
        "    print(\"else\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "usFzNDJE_l6n",
        "outputId": "6d67484c-d17c-42ee-d18f-a3d250c692c5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "four\n",
            "five\n"
          ]
        }
      ],
      "source": [
        "x = \"1\"\n",
        "\n",
        "if x == 1:\n",
        "    print(\"one\")\n",
        "elif x == \"1\":\n",
        "    if int(x) > 1:\n",
        "        print(\"two\")\n",
        "    elif int(x) < 1:\n",
        "        print(\"three\")\n",
        "    else:\n",
        "        print(\"four\")\n",
        "\n",
        "if int(x) == 1:\n",
        "    print(\"five\")\n",
        "else:\n",
        "    print(\"six\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y1GHxKsx_l6n",
        "outputId": "ea31951f-61bd-4e53-e57e-ea4f97e03051"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "one\n",
            "three\n"
          ]
        }
      ],
      "source": [
        "x = 1\n",
        "y = 1.0\n",
        "z = \"1\"\n",
        "\n",
        "if x == y:\n",
        "    print(\"one\")\n",
        "if y == z:\n",
        "    print(\"two\")\n",
        "    print(x)\n",
        "    print(y)\n",
        "elif x == y:\n",
        "    print(\"three\")\n",
        "else:\n",
        "    print(\"four\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "z2tXnK82_l6s"
      },
      "source": [
        "## 3.2 Struktur perulangan\n",
        "\n",
        "Python menyediakan dua statement untuk melakukan proses perulangan yaitu for dan while. Diantara kedua statement ini, secara umum for lebih banyak digunakan daripada while.\n",
        "\n",
        "### 1. Statement while\n",
        "\n",
        "Sama seperti kebanyakan bahasa pemrograman lainnya, Python juga mendukung statement while untuk melakukan perulangan satu atau sekelompok statement. Bentuk umum dari perulangan while adalah sebagai berikut :\n",
        "\n",
        "```python\n",
        "while kondisi:\n",
        "    statement1\n",
        "    statement2\n",
        "    statement1\n",
        "    :\n",
        "    :\n",
        "    statementn\n",
        "```\n",
        "Pada bentuk perulangan diatas, statement1, statement2 dan seterusnya merupakan sekelompok statement yang akan diulang. Statement tersebut akan terus dieksekusi/ diulang selama kondisi bernilai True. Maka diperlukan sebuah statement yang akan bernilai False, agar proses dapat berhenti. Perhatikan syntax berikut :\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g_NSKHk1_l6s",
        "outputId": "6b5b36cc-8b26-4b35-8db8-ce66b8ea5ac2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "9\n",
            "25\n",
            "49\n",
            "81\n"
          ]
        }
      ],
      "source": [
        "i = 1\n",
        "\n",
        "while i<10:\n",
        "    print(i**2)\n",
        "    i = i+2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pgAmyXHi_l6t"
      },
      "source": [
        "#### Perhatikan contoh program untuk menghitung berapa ganjil dan genap dari rangkaian bilangan :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9OMsf_Xw_l6t",
        "outputId": "a7f73411-5ae8-40bf-968a-63a72dd1ac27"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number or type 0 to stop: 81\n",
            "Enter a number or type 0 to stop: 9\n",
            "Enter a number or type 0 to stop: 1\n",
            "Enter a number or type 0 to stop: 0\n",
            "Odd numbers count: 3\n",
            "Even numbers count: 0\n"
          ]
        }
      ],
      "source": [
        "# program that reads a sequence of numbers\n",
        "# and counts how many numbers are even and how many are odd\n",
        "# program terminates when zero is entered\n",
        "\n",
        "oddNumbers = 0\n",
        "evenNumbers = 0\n",
        "\n",
        "# read the first number\n",
        "number = int(input(\"Enter a number or type 0 to stop: \"))\n",
        "\n",
        "# 0 terminates execution\n",
        "while number != 0:\n",
        "    # check if the number is odd\n",
        "    if number % 2 == 1:\n",
        "        # increase the oddNumbers counter\n",
        "        oddNumbers += 1\n",
        "    else:\n",
        "        # increase the evenNumbers counter\n",
        "        evenNumbers += 1\n",
        "    # read the next number\n",
        "    number = int(input(\"Enter a number or type 0 to stop: \"))\n",
        "\n",
        "# print results\n",
        "print(\"Odd numbers count:\", oddNumbers)\n",
        "print(\"Even numbers count:\", evenNumbers)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nclrD_ui_l6t"
      },
      "source": [
        "## Latihan\n",
        "A junior magician has picked a secret number. He has hidden it in a variable named `secretNumber`. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.\n",
        "\n",
        "Your task is to help the magician complete the code in the editor in such a way so that the code:\n",
        "\n",
        "- will ask the user to enter an integer number;\n",
        "- will use a `while` loop;\n",
        "- will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message `\"Ha ha! You're stuck in my loop!\"` and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: `\"Well done, muggle! You are free now.\"`\n",
        "\n",
        "```python\n",
        "secretNumber = 777\n",
        "\n",
        "print(\n",
        "\"\"\"\n",
        "+================================+\n",
        "| Welcome to my game, muggle!    |\n",
        "| Enter an integer number        |\n",
        "| and guess what number I've     |\n",
        "| picked for you.                |\n",
        "| So, what is the secret number? |\n",
        "+================================+\n",
        "\"\"\")\n",
        "```\n",
        "\n",
        "The magician is counting on you! Don't disappoint him."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nDev1y7m_l6t",
        "outputId": "88804c1c-72af-4884-8e67-910b60ad8bdd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Input angka rahasia untuk berhenti : 777\n",
            "Well done, Congrats...\n"
          ]
        }
      ],
      "source": [
        "secretNum = 777\n",
        "\n",
        "guessNum = 0\n",
        "\n",
        "while guessNum != secretNum:\n",
        "    guessNum = int(input(\"Input angka rahasia untuk berhenti : \"))\n",
        "    if guessNum != secretNum:\n",
        "        print(\"Perulangan akan terus lanjut...\")\n",
        "\n",
        "print(\"Well done, Congrats...\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bGb4lOF2_l6t"
      },
      "source": [
        "### 2. Statement for\n",
        "\n",
        "Selain menggunakan statement while, kita juga dapat melakukan perulangan dengan statement for. Perintah for biasanya digunakan untuk mengambil atau menelusuri data (item) yang terdapat pada tipe-tipe koleksi seperti string, list, tuple, dictionary dan set. Dalam pemrograman, proses penelusuran data dalam sebuah koleksi disebut iterasi. Selain itu, for juga dapat melakukan perulangan normal (sama seperti while), yaitu dengan menggunakan fungsi range(). Dengan menggunakan range(), kita akan dapat dengan mudah melakukan perulangan dari indeks awal ke indeks tertentu.\n",
        "\n",
        "Bentuk perintah for dapat dituliskan sebagai berikut :\n",
        "\n",
        "1. Statement for untuk perintah koleksi\n",
        "```python\n",
        "for indeks tipe koleksi:\n",
        "    statement1\n",
        "    statement2\n",
        "    ...\n",
        "```\n",
        "2. Statement for untuk rentang nilai tertentu\n",
        "```python\n",
        "for indeks in range (nilai_awal, nilai_akhir, step):\n",
        "    statement1\n",
        "    statement2\n",
        "    ...\n",
        "```\n",
        "Perhatikan contoh-contoh dibawah ini :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ga2mlnaD_l6u",
        "outputId": "f4e4abd9-d4e1-4cb5-959e-5f22b6b45e23"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n"
          ]
        }
      ],
      "source": [
        "for i in range(5):\n",
        "    print(i)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qytHPMg6_l6u",
        "outputId": "c2fe4825-23f1-4d08-9238-559a6d01a4e8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n"
          ]
        }
      ],
      "source": [
        "for i in range(2,8):\n",
        "    print(i)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oJk2ZuRf_l6u",
        "outputId": "eb90638b-5cc6-48f7-9c8a-2295b590392c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "5\n",
            "8\n",
            "11\n",
            "14\n",
            "17\n"
          ]
        }
      ],
      "source": [
        "for i in range(2,18,3):\n",
        "    print(i)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C6a0znH__l6u",
        "outputId": "7787a28a-eb53-41da-f5a4-ea7141227bec"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "masuk else\n"
          ]
        }
      ],
      "source": [
        "for i in range(5):\n",
        "    print(i)\n",
        "else:\n",
        "    print(\"masuk else\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5aZsU38i_l6u"
      },
      "source": [
        "## Latihan\n",
        "\n",
        "\n",
        "Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!\n",
        "\n",
        "The word Mississippi is also used for a slightly different purpose: to count mississippily.\n",
        "\n",
        "If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.\n",
        "\n",
        "The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore \"one Mississippi, two Mississippi, three Mississippi\" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.\n",
        "\n",
        "\n",
        "Your task is very simple here: write a program that uses a for loop to \"count mississippily\" to five. Having counted to five, the program should print to the screen the final message \"Ready or not, here I come!\"\n",
        "\n",
        "Use the skeleton we've provided in the editor.\n",
        "\n",
        "```python\n",
        "import time\n",
        "\n",
        "# Write a for loop that counts to five.\n",
        "    # Body of the loop - print the loop iteration number and the word \"Mississippi\".\n",
        "    # Body of the loop - use: time.sleep(1)\n",
        "\n",
        "# Write a print function with the final message.\n",
        "```\n",
        "\n",
        "<strong> EXTRA INFO </strong>\n",
        "\n",
        "Note that the code in the editor contains two elements which may not be fully clear to you at this moment: the import time statement, and the sleep() method. We're going to talk about them soon.\n",
        "\n",
        "For the time being, we'd just like you to know that we've imported the time module and used the sleep() method to suspend the execution of each subsequent print() function inside the for loop for one second, so that the message outputted to the console resembles an actual counting. Don't worry - you'll soon learn more about modules and methods."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pAaXKltD_l6u",
        "outputId": "b41433e4-0667-4453-9844-201fa8ebd70c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0  Missisipi\n",
            "1  Missisipi\n",
            "2  Missisipi\n",
            "3  Missisipi\n",
            "4  Missisipi\n"
          ]
        }
      ],
      "source": [
        "import time\n",
        "\n",
        "for i in range(5):\n",
        "    print(i,\" Missisipi\")\n",
        "    time.sleep(1)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-OJ8qBkj_l6v"
      },
      "source": [
        "### 3. Statement Loncat\n",
        "\n",
        "Statement loncat merupakan perintah yang digunakan untuk memindahkan eksekusi program dari satu bagian tertentu ke bagian lain. Python menyediakan tiga statement yaitu : break, continue dan return.\n",
        "\n",
        "#### 3.1 Statement break\n",
        "\n",
        "Statement break digunakan untuk menghentikan secara paksa proses perulangan, meskipun kondisi perulangan sebenarnya masih bernilai True. Perhatikan contoh-contoh berikut ini :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7ClCSoZW_l6v",
        "outputId": "60d41f1c-6cf6-4fe4-ee13-6c8ca3ffa2b4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 1 2 3 4 5 6 7  masih dalam for\n"
          ]
        }
      ],
      "source": [
        "for i in range (11):\n",
        "    print(i, end=\" \")\n",
        "    if i==7:\n",
        "        print(\" masih dalam for\")\n",
        "        break"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BaajLC0v_l6v",
        "outputId": "09167c19-1c8c-4f49-aa81-96e63a2cd927"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The break instruction:\n",
            "Inside the loop. 1\n",
            "Inside the loop. 2\n",
            "Outside the loop.\n"
          ]
        }
      ],
      "source": [
        "# break - example\n",
        "\n",
        "print(\"The break instruction:\")\n",
        "for i in range(1, 6):\n",
        "    if i == 3:\n",
        "        break\n",
        "    print(\"Inside the loop.\", i)\n",
        "print(\"Outside the loop.\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mFynJ_-y_l6v",
        "outputId": "71dc53ea-0f1a-4717-81d0-594621409c86"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number or type -1 to end program: -1\n",
            "You haven't entered any number.\n"
          ]
        }
      ],
      "source": [
        "largestNumber = -99999999\n",
        "counter = 0\n",
        "\n",
        "while True:\n",
        "    number = int(input(\"Enter a number or type -1 to end program: \"))\n",
        "    if number == -1:\n",
        "        break\n",
        "    counter += 1\n",
        "    if number > largestNumber:\n",
        "        largestNumber = number\n",
        "\n",
        "if counter != 0:\n",
        "    print(\"The largest number is\", largestNumber)\n",
        "else:\n",
        "    print(\"You haven't entered any number.\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KBjfDV6N_l6v"
      },
      "source": [
        "#### 3.2 Statement continue\n",
        "\n",
        "Statement continue berguna untuk memaksa pengulangan agar memroses indeks selanjutnya meskipun statement didalam blok pengulangan sebenarna belum semua di eksekusi. Dengan kata lain, statement yang ada dibawah statement continue akan diabaikan (tidak dieksekusi)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u12tQr2p_l6v",
        "outputId": "1f90dd7d-2493-4557-c46b-e8f3179f9a64"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\t3\t5\t7\t9\t"
          ]
        }
      ],
      "source": [
        "for i in range (1,11):\n",
        "    if i % 2 ==0:\n",
        "        continue\n",
        "    print(i, end=\"\\t\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HiM4HtAX_l6w",
        "outputId": "39bb755c-d8e8-4d39-e4d4-f29704f5194e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n"
          ]
        }
      ],
      "source": [
        "for i in range (1,11):\n",
        "    if i % 2 ==0:\n",
        "        print(i)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AtqjTOSM_l6w",
        "outputId": "1138f3f4-8b53-41e4-953a-70bb77355ff3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "The continue instruction:\n",
            "Inside the loop. 1\n",
            "Inside the loop. 2\n",
            "Inside the loop. 4\n",
            "Inside the loop. 5\n",
            "Outside the loop.\n"
          ]
        }
      ],
      "source": [
        "# continue - example\n",
        "\n",
        "print(\"\\nThe continue instruction:\")\n",
        "for i in range(1, 6):\n",
        "    if i == 3:\n",
        "        continue\n",
        "    print(\"Inside the loop.\", i)\n",
        "print(\"Outside the loop.\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H3YfcrBI_l6w",
        "outputId": "0b15f031-2743-4d28-a41e-48935a861c25"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number or type -1 to end program: 0\n",
            "Enter a number or type -1 to end program: -1\n",
            "The largest number is 0\n"
          ]
        }
      ],
      "source": [
        "largestNumber = -99999999\n",
        "counter = 0\n",
        "\n",
        "number = int(input(\"Enter a number or type -1 to end program: \"))\n",
        "\n",
        "while number != -1:\n",
        "    if number == -1:\n",
        "        continue\n",
        "    counter += 1\n",
        "\n",
        "    if number > largestNumber:\n",
        "        largestNumber = number\n",
        "    number = int(input(\"Enter a number or type -1 to end program: \"))\n",
        "\n",
        "if counter:\n",
        "    print(\"The largest number is\", largestNumber)\n",
        "else:\n",
        "    print(\"You haven't entered any number.\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e0XG2hbt_l6w"
      },
      "source": [
        "## Latihan\n",
        "\n",
        "The `break` statement is used to exit/terminate a loop.\n",
        "\n",
        "Design a program that uses a `while` loop and continuously asks the user to enter a word unless the user enters `\"chupacabra\"` as the secret exit word, in which case the message `\"You've successfully left the loop.\"` should be printed to the screen, and the loop should terminate.\n",
        "\n",
        "Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 36,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XOPuCCx__l6w",
        "outputId": "2cbf7ef8-851f-4baf-8d4b-a2a00b6c1262"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan Sebuah Kata untuk keluar dari perulangan = chupacabra\n",
            "You've successfully left the loop\n"
          ]
        }
      ],
      "source": [
        "while True:\n",
        "    word = input(\"Masukkan Sebuah Kata untuk keluar dari perulangan = \")\n",
        "    if(word==\"chupacabra\"):\n",
        "        break\n",
        "\n",
        "print(\"You've successfully left the loop\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gmjqVIE8_l6w"
      },
      "source": [
        "## Latihan\n",
        "\n",
        "\n",
        "The `continue` statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.\n",
        "\n",
        "It can be used with both the while and for loops.\n",
        "\n",
        "Your task here is very special: you must design a vowel eater! Write a program that uses:\n",
        "\n",
        "- a for loop;\n",
        "- the concept of conditional execution (if-elif-else)\n",
        "- the continue statement.\n",
        "\n",
        "Your program must:\n",
        "\n",
        "- ask the user to enter a word;\n",
        "- use `userWord = userWord.upper()` to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the `upper()` method very soon - don't worry;\n",
        "- use conditional execution and the `continue` statement to \"eat\" the following vowels A, E, I, O, U from the inputted word;\n",
        "- print the uneaten letters to the screen, each one of them on a separate line.\n",
        "\n",
        "```python\n",
        "# Prompt the user to enter a word\n",
        "# and assign it to the userWord variable.\n",
        "\n",
        "for letter in userWord:\n",
        "    # Complete the body of the for loop.\n",
        "```\n",
        "\n",
        "Test your program with the data we've provided for you.\n",
        "\n",
        "\n",
        "Test data\n",
        "\n",
        "Sample input: `Gregory`\n",
        "\n",
        "Expected output:\n",
        "```\n",
        "G\n",
        "R\n",
        "G\n",
        "R\n",
        "Y\n",
        "```\n",
        "Sample input: `abstemious`\n",
        "\n",
        "Expected output:\n",
        "```\n",
        "B\n",
        "S\n",
        "T\n",
        "M\n",
        "S\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 37,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a4G9Qq1T_l6x",
        "outputId": "9b2ec6a1-4125-4a89-d54c-2c63ced7f509"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan sebuah kata = aku\n",
            "K\n"
          ]
        }
      ],
      "source": [
        "# Prompt the user to enter a word\n",
        "# and assign it to the userWord variable.\n",
        "userWord = input(\"Masukkan sebuah kata = \")\n",
        "\n",
        "for letter in userWord:\n",
        "    if letter.upper() in ['A','I','U','E','O']:\n",
        "        continue\n",
        "\n",
        "    print(letter.upper())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kbf8JEDD_l6x"
      },
      "source": [
        "## Latihan\n",
        "\n",
        "Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.\n",
        "\n",
        "Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.\n",
        "\n",
        "The figure illustrates the rule used by the builders:\n",
        "```\n",
        "=\n",
        "==\n",
        "===\n",
        "```\n",
        "blocks : 6\n",
        "height : 3\n",
        "Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.\n",
        "\n",
        "Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.\n",
        "\n",
        "Test your code using the data we've provided.\n",
        "\n",
        "Sample input: 6\n",
        "\n",
        "Expected output: The height of the pyramid: 3\n",
        "\n",
        "Sample input: 20\n",
        "\n",
        "Expected output: The height of the pyramid: 5\n",
        "\n",
        "Sample input: 1000\n",
        "\n",
        "Expected output: The height of the pyramid: 44\n",
        "\n",
        "Sample input: 2\n",
        "\n",
        "Expected output: The height of the pyramid: 1"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 38,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-VUQiRFX_l6x",
        "outputId": "83e8c6f3-da8e-4dd2-d607-79da1347c5ea"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of blocks: 6\n",
            "The height of the pyramid: 3\n"
          ]
        }
      ],
      "source": [
        "blocks = int(input(\"Enter the number of blocks: \"))\n",
        "current_block = 0\n",
        "height = 0\n",
        "i=0\n",
        "\n",
        "while i<blocks:\n",
        "    height += 1\n",
        "    current_block += height\n",
        "    # print(i,current_block)\n",
        "    if current_block> blocks:\n",
        "        break\n",
        "\n",
        "height -= 1\n",
        "\n",
        "print(\"The height of the pyramid:\", height)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9HVgBv4N_l6x"
      },
      "source": [
        "### Latihan\n",
        "\n",
        "1. Buatlah perulangan dengan menggunakan for yang mulai dari 0 sampai dengan 10, dan cetak nomer ganjil pada layar.\n",
        "\n",
        "2. Buatlah perulangan dengan menggunakan while dari 0 sampai dengan 10, dan cetak nomer ganjil pada layar\n",
        "\n",
        "3. Buatlah sebuah program dengan perulangan for dan statement break. Program harus diiterasi sebanyak jumlah karakter didalam sebuah alamat email, dan loop akan berhenti jika menemukan simbol '@' dan cetak karakter yang ditemukan sebelum simbol '@' didalam sebuah line\n",
        "\n",
        "4. Buatlah sebuah perulangan loop dan statement continue. Program harus diiterasi sebanyak nomer yang ditemukan dalam string (digit = \"0165031806510\"), ganti 0 dengan x, lalu cetak string yang telah dimodifikasi."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 39,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wYMP-LkF_l6x",
        "outputId": "9ff08a0c-2630-4a5f-81ec-b46f50090198"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 3 5 7 9 "
          ]
        }
      ],
      "source": [
        "for i in range(1, 11):\n",
        "    if i % 2 !=0:\n",
        "        print(i,end=' ')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 40,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mgba1IIB_l6y",
        "outputId": "af0fec0b-384e-44f4-feb9-f55e94badd9a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 3 5 7 9 "
          ]
        }
      ],
      "source": [
        "x=1\n",
        "while x<11:\n",
        "    if x % 2 !=0:\n",
        "        print(x,end=' ')\n",
        "    x +=1"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 41,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ojDggva0_l6y",
        "outputId": "c0847d19-c7f6-4ec8-896d-7453094a305f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "r a t n a . l e s t a r i "
          ]
        }
      ],
      "source": [
        "for ch in \"ratna.lestari@ugm.ac.id\":\n",
        "    if ch == \"@\":\n",
        "        break\n",
        "    print(ch,end=' ')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 42,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6qqklemQ_l6y",
        "outputId": "9ab4f6ff-9883-42d1-b1fa-92bfdd6402cb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "x\n",
            "1\n",
            "6\n",
            "5\n",
            "x\n",
            "3\n",
            "1\n",
            "8\n",
            "x\n",
            "6\n",
            "5\n",
            "1\n",
            "x\n"
          ]
        }
      ],
      "source": [
        "for digit in \"0165031806510\":\n",
        "    if digit == \"0\":\n",
        "        print (\"x\")\n",
        "        continue\n",
        "    print(digit)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7lm6gFBm_l6y"
      },
      "source": [
        "#### Apakah output dari kode-kode berikut?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 43,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_3iEzQWy_l6y",
        "outputId": "6d3a74a2-0be7-4bef-e441-4e5ae5622090"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "3\n",
            "2\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "n = 3\n",
        "\n",
        "while n > 0:\n",
        "    print(n + 1)\n",
        "    n -= 1\n",
        "else:\n",
        "    print(n)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 44,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iPtLRea6_l6y",
        "outputId": "acca0526-23d5-42ce-ca4c-46fee2812351"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-1\n",
            "0\n",
            "1\n",
            "2\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "n = range(4)\n",
        "\n",
        "for num in n:\n",
        "    print(num - 1)\n",
        "else:\n",
        "    print(num)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 45,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QcdWCoxR_l6y",
        "outputId": "29db0ad5-a4c1-4fc0-f794-3ae63bc0f0a3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "for i in range(0, 6, 3):\n",
        "    print(i)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QRd7XCK8_l6y"
      },
      "source": [
        "## 3.3 Operasi Logika\n",
        "\n",
        "Operasi Logika `and`\n",
        "\n",
        "| Argument A | Argument B | A and B |\n",
        "|------------|------------|---------|\n",
        "| False      | False      | False   |\n",
        "| False      | True       | False   |\n",
        "| True       | False      | False   |\n",
        "| True       | True       | True    |\n",
        "\n",
        "Operasi Logika `or`\n",
        "\n",
        "| Argument A | Argument B | A or B |\n",
        "|------------|------------|--------|\n",
        "| False      | False      | False  |\n",
        "| False      | True       | True   |\n",
        "| True       | False      | True   |\n",
        "| True       | True       | True   |\n",
        "\n",
        "Operasi Logika `not`\n",
        "\n",
        "| Argument | not Argument |\n",
        "|----------|--------------|\n",
        "| False    | True         |\n",
        "| True     | False        |\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8bm8iZj4_l6z"
      },
      "source": [
        "> If we have some free time, <b>and</b> the weather is good, we will go for a walk\n",
        "\n",
        "> If you are in the mall <b>or</b> I am in the mall, one of us will buy a gift for Mom.\n",
        "\n",
        "Perhatikan contoh dibawah ini :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 46,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hj31U-Zv_l6z",
        "outputId": "729cc0ef-5784-4f32-aef2-36b593bd37cc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ],
      "source": [
        "x = 1\n",
        "y = 0\n",
        "\n",
        "z = ((x == y) and (x == y)) or not(x == y)\n",
        "print(not(z))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7YkWA1Uu_l6z"
      },
      "source": [
        "## 3.4 List dan Array\n",
        "\n",
        "Tipe list dalam python sebenernya mirip dengan array normal pada bahasa pemrograman lain. List juga dapat menampung beberapa tipe data sekaligus.\n",
        "\n",
        "Bentuk umum untuk membuat list dalam python adalah :\n",
        "\n",
        "```python\n",
        "\n",
        "nama_list = [nilai1, nilai2, nilai3,...]\n",
        "```\n",
        "\n",
        "Perhatikan contoh dibawah ini :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 47,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F_d2MSfL_l6z",
        "outputId": "f7a305f7-9062-4cb7-f1ec-75a5c6e918c1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5]\n"
          ]
        }
      ],
      "source": [
        "var1=1\n",
        "var2=2\n",
        "var3=3\n",
        "var4=4\n",
        "var5=5\n",
        "\n",
        "#bandingkan\n",
        "\n",
        "var=[1,2,3,4,5]\n",
        "print(var)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "clO0VgLY_l6z"
      },
      "source": [
        "### Indexing List\n",
        "Dalam list, elemen tidak diindeks berdasarkan key tertentu yang namanya bisa didefinisikan sendiri melainkan berdasarkan indeks bilangan yang diawali dengan nilai nol(0). Perhatikan contoh berikut :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 48,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3T6h9Mco_l6z",
        "outputId": "62e46d38-fe44-4413-a563-8ffae48d3c3b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 3, 4, 5]\n",
            "4\n",
            "5\n"
          ]
        }
      ],
      "source": [
        "num = [2,3,4,5]\n",
        "print(num)\n",
        "print(num[2])\n",
        "print(num[-1])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "USwyOU3j_l6z"
      },
      "source": [
        "Indeks dapat juga bernilai negatif yaitu menghitung indeks mulai dari kanan. Perhatikan contoh berikut :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 49,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lyANdwoO_l60",
        "outputId": "d4634b6e-c44d-4cba-d4c7-25eed35c5db2"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "500\n",
            "400\n",
            "100\n",
            "\n",
            "\n",
            "500\n",
            "400\n",
            "100\n"
          ]
        }
      ],
      "source": [
        "lst = [100,200,300,400,500]\n",
        "print(lst[-1])\n",
        "print(lst[-2])\n",
        "print(lst[-5])\n",
        "\n",
        "print(\"\\n\")\n",
        "print(lst[4])\n",
        "print(lst[3])\n",
        "print(lst[0])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4nK2E-B8_l60"
      },
      "source": [
        "## Slicing List"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 50,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8rHE-MG__l60",
        "outputId": "874f9fde-b98b-4a68-bcbe-e323beca5526"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[4, 1, 6]\n",
            "[1, 6]\n",
            "[9, 10, 8]\n",
            "[4, 1, 6]\n",
            "[4, 1, 6, 9, 10, 8]\n"
          ]
        }
      ],
      "source": [
        "lst=[4,1,6,9,10,8]\n",
        "\n",
        "print(lst[0:3])\n",
        "print(lst[1:3])\n",
        "\n",
        "print(lst[-3:])\n",
        "print(lst[:-3])\n",
        "\n",
        "print(lst[:])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "m5v_8d3f_l60"
      },
      "source": [
        "### Swap\n",
        "\n",
        "Nilai elemen didalam list selain dapat diakses juga dapat dimanipulasi dengan swapping. Perhatikan contoh berikut :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 51,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GE0_0fZh_l60",
        "outputId": "d6946f4a-4e47-408d-e0eb-5d740e6e1281"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[3, 2, 4]\n"
          ]
        }
      ],
      "source": [
        "num=[2,3,4]\n",
        "num[0],num[1] = num[1], num[0]\n",
        "print(num)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nmDSzmy9_l60"
      },
      "source": [
        "#### Bubble Short\n",
        "![BubbleSort_worst_case.gif](attachment:BubbleSort_worst_case.gif)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 52,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LGYGknFY_l60",
        "outputId": "69aca38e-0da0-4f7d-84bf-dc3e23b9306c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 4, 6, 8, 10]\n"
          ]
        }
      ],
      "source": [
        "myList = [8, 10, 6, 2, 4] # list to sort\n",
        "swapped = True # it's a little fake - we need it to enter the while loop\n",
        "\n",
        "while swapped:\n",
        "    swapped = False # no swaps so far\n",
        "    for i in range(len(myList) - 1):\n",
        "        if myList[i] > myList[i + 1]:\n",
        "            swapped = True # swap occured!\n",
        "            myList[i], myList[i + 1] = myList[i + 1], myList[i]\n",
        "\n",
        "print(myList)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KA00xxUD_l60"
      },
      "source": [
        "### Lab 3.4.1.6: The basics of lists\n",
        "There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.\n",
        "\n",
        "Your task is to:\n",
        "\n",
        "- write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (step 1)\n",
        "- write a line of code that removes the last element from the list (step 2)\n",
        "- write a line of code that prints the length of the existing list (step 3.)\n",
        "Ready for this challenge?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 53,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8DmdVio9_l61",
        "outputId": "4c601350-e506-4c66-e259-dae9c76e69f9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5]\n"
          ]
        }
      ],
      "source": [
        "hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.\n",
        "\n",
        "# Step 1: write a line of code that prompts the user\n",
        "# to replace the middle number with an integer number entered by the user.\n",
        "\n",
        "# Step 2: write a line of code here that removes the last element from the list.\n",
        "\n",
        "# Step 3: write a line of code here that prints the length of the existing list.\n",
        "\n",
        "print(hatList)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RBPOsRTp_l61"
      },
      "source": [
        "### Menambah Elemen ke dalam list\n",
        "\n",
        "Terdapat tiga cara untuk menambahkan elemen baru kedalam sebuah list yaitu :\n",
        "\n",
        " - Menggunakan metode append() : Metode ini digunakan untuk menambah elemen tunggal dibagian akhir list. Perhatikan contoh dibawah :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 54,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gZT75H5K_l61",
        "outputId": "a2bd1a25-0493-43c3-9ed6-8d961f50bda6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Salak', 'Mangga', 'Apel', 'Jeruk']\n"
          ]
        }
      ],
      "source": [
        "buah=[\"Salak\",\"Mangga\",\"Apel\"]\n",
        "buah.append(\"Jeruk\")\n",
        "print(buah)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 55,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MNmfObAB_l61",
        "outputId": "aa1d5ce6-7f10-4211-976a-0edfc1749e7f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5]\n"
          ]
        }
      ],
      "source": [
        "myList = [] # creating an empty list\n",
        "\n",
        "for i in range(5):\n",
        "    myList.append(i + 1)\n",
        "\n",
        "print(myList)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bZ89gxTQ_l61"
      },
      "source": [
        "`Menggunakan metode insert() : Metode ini digunakan untuk menambah elemen tunggal di indeks / posisi tertentu. Perhatikan contoh dibawah :`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 56,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xfXjuioK_l61",
        "outputId": "365b3cf8-4578-4a10-c58f-637e91f17307"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['durian', 'kiwi', 'mangga', 'apel']\n"
          ]
        }
      ],
      "source": [
        "buah = [\"durian\", \"mangga\", \"apel\"]\n",
        "buah.insert(1,\"kiwi\")\n",
        "print (buah)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 57,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jF-lqxTn_l61",
        "outputId": "72a0510a-e260-4b24-d0c4-55490cd4bb59"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "[111, 7, 2, 1]\n",
            "5\n",
            "[111, 7, 2, 1, 4]\n",
            "6\n",
            "[222, 111, 7, 2, 1, 4]\n"
          ]
        }
      ],
      "source": [
        "numbers = [111, 7, 2, 1]\n",
        "print(len(numbers))\n",
        "print(numbers)\n",
        "\n",
        "###\n",
        "\n",
        "numbers.append(4)\n",
        "\n",
        "print(len(numbers))\n",
        "print(numbers)\n",
        "\n",
        "###\n",
        "\n",
        "numbers.insert(0, 222)\n",
        "print(len(numbers))\n",
        "print(numbers)\n",
        "\n",
        "#"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "N_jKNOMW_l61"
      },
      "source": [
        "### Menghapus Elemen kedalam list\n",
        "\n",
        "Menghapus elemen dapat dilakukan dengan :\n",
        "\n",
        "```python\n",
        "nama_list.remove(nilai)\n",
        "```\n",
        "\n",
        "atau dengan memberikan indeksnya menggunakan instruksi delete :\n",
        "\n",
        "```python\n",
        "del nama_list[indeks]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 58,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YAa-SP1p_l61",
        "outputId": "5ce3d535-a759-44d2-8754-e39b42a08e87"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[5, 3, 2, 1]\n"
          ]
        }
      ],
      "source": [
        "num = [5,4,3,2,1]\n",
        "\n",
        "del num[1]\n",
        "print(num)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "x1NPw4Pn_l61"
      },
      "source": [
        "## Latihan\n",
        "\n",
        "The Beatles were one of the most popular music group of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.\n",
        "\n",
        "The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).\n",
        "\n",
        "\n",
        "Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:\n",
        "\n",
        "- step 1: create an empty list named `beatles`;\n",
        "- step 2: use the `append()` method to add the following members of the band to the list: `John Lennon`, `Paul McCartney`, and `George Harrison`;\n",
        "- step 3: use the `for` loop and the `append()` method to prompt the user to add the following members of the band to the list: `Stu Sutcliffe`, and `Pete Best`;\n",
        "- step 4: use the `del` instruction to remove `Stu Sutcliffe` and `Pete Best` from the list;\n",
        "- step 5: use the `insert()` method to add `Ringo Starr` to the beginning of the list.\n",
        "By the way, are you a Beatles fan?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 59,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fZ_6Jawm_l62",
        "outputId": "ba7ec999-59f1-465e-edbc-b3c81036b644"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Step 1: []\n",
            "Step 2: ['John Lennon', 'Paul McCartney', 'George Harrison']\n",
            "Masukkan anggota baru = nanda\n",
            "Masukkan anggota baru = JohnLennon\n",
            "Step 3: ['John Lennon', 'Paul McCartney', 'George Harrison', 'nanda', 'JohnLennon']\n",
            "Step 4: ['John Lennon', 'Paul McCartney', 'George Harrison']\n",
            "Step 5: ['Ringo Starr', 'John Lennon', 'Paul McCartney', 'George Harrison']\n",
            "The Fab 4\n"
          ]
        }
      ],
      "source": [
        "# step 1\n",
        "beatles = []\n",
        "print(\"Step 1:\", beatles)\n",
        "\n",
        "# step 2\n",
        "beatles.append(\"John Lennon\")\n",
        "beatles.append(\"Paul McCartney\")\n",
        "beatles.append(\"George Harrison\")\n",
        "print(\"Step 2:\", beatles)\n",
        "\n",
        "# step 3\n",
        "for i in range(2):\n",
        "    nama = input(\"Masukkan anggota baru = \")\n",
        "    beatles.append(nama)\n",
        "print(\"Step 3:\", beatles)\n",
        "\n",
        "# step 4\n",
        "del beatles[-2:]\n",
        "print(\"Step 4:\", beatles)\n",
        "\n",
        "# step 5\n",
        "beatles.insert(0,\"Ringo Starr\")\n",
        "print(\"Step 5:\", beatles)\n",
        "\n",
        "\n",
        "# testing list legth\n",
        "print(\"The Fab\", len(beatles))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sc_ZYAYT_l62"
      },
      "source": [
        "## Tambahan Method"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 60,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sc3wiAMR_l62",
        "outputId": "041feaa6-903f-4c14-a722-e1c6b7ff612a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[5, 1, 3, 2, 10]\n",
            "[1, 2, 3, 5, 10]\n",
            "[10, 5, 3, 2, 1]\n"
          ]
        }
      ],
      "source": [
        "lst = [5, 1, 3, 2, 10]\n",
        "print(lst)\n",
        "lst.sort()\n",
        "print(lst)\n",
        "lst.reverse()\n",
        "print(lst)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 61,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DfMgN3vM_l62",
        "outputId": "59cb74bb-3fd2-49de-e500-f261af70fb3e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['car', 'bicycle', 'motor']\n",
            "['bicycle', 'motor']\n",
            "['bicycle', 'motor']\n"
          ]
        }
      ],
      "source": [
        "vehiclesOne = ['car', 'bicycle', 'motor']\n",
        "print(vehiclesOne) # outputs: ['car', 'bicycle', 'motor']\n",
        "\n",
        "vehiclesTwo = vehiclesOne\n",
        "del vehiclesOne[0] # deletes 'car'\n",
        "print(vehiclesTwo) # outputs: ['bicycle', 'motor']\n",
        "print(vehiclesOne)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 62,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l0BqAXX2_l62",
        "outputId": "c7e392f4-6429-4103-eca9-01e62f3f4d71"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['car', 'bicycle', 'motor']\n",
            "['car', 'bicycle', 'motor']\n",
            "['bicycle', 'motor']\n"
          ]
        }
      ],
      "source": [
        "vehiclesOne = ['car', 'bicycle', 'motor']\n",
        "print(vehiclesOne) # outputs: ['car', 'bicycle', 'motor']\n",
        "\n",
        "vehiclesTwo = vehiclesOne[:]\n",
        "del vehiclesOne[0] # deletes 'car'\n",
        "print(vehiclesTwo) # outputs: ['bicycle', 'motor']\n",
        "print(vehiclesOne)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 63,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gRYX9DaQ_l62",
        "outputId": "614d2950-5b70-4c52-d9dd-35b4948d3220"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "Nama Budi ada di list\n"
          ]
        }
      ],
      "source": [
        "nama = [\"Ana\",\"Budi\",\"Citra\"]\n",
        "kata_kunci = \"Budi\"\n",
        "\n",
        "print(kata_kunci not in nama)\n",
        "\n",
        "if kata_kunci in nama:\n",
        "    print(\"Nama \"+kata_kunci+\" ada di list\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 64,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AMK7VGcV_l62",
        "outputId": "0508f6ad-38e1-4205-87e7-ae77cba6ab2c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 1 2 3 4 5 6 7 8 9 \n",
            "1 2 3 4 5 6 \n",
            "1 3 5 7 9 \n",
            "10 8 6 4 2 0 -2 -4 -6 -8 "
          ]
        }
      ],
      "source": [
        "for i in range(10):\n",
        "    print(i, end=\" \")\n",
        "\n",
        "print()\n",
        "for i in range(1,7):\n",
        "    print(i, end=\" \")\n",
        "\n",
        "print()\n",
        "for i in range(1,10,2):\n",
        "    print(i, end=\" \")\n",
        "\n",
        "print()\n",
        "for i in range(10,-10,-2):\n",
        "    print(i, end=\" \")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 65,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "23PHor6H_l63",
        "outputId": "3fef7fbd-eb06-4e9f-aeee-957024cc59e9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 3 5 7 9 "
          ]
        }
      ],
      "source": [
        "for i in range(1, 11):\n",
        "    if i%2 != 0:\n",
        "        print(i, end=\" \")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 66,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lb5GkCUP_l63",
        "outputId": "953b5b8f-4017-4140-9606-0be2579dd0fd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 3 5 7 9 "
          ]
        }
      ],
      "source": [
        "x = 1\n",
        "while x < 11:\n",
        "    if x%2!=0:\n",
        "        print(x, end=\" \")\n",
        "    x += 1"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 67,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CSV39RHn_l63",
        "outputId": "88f39c1b-46b5-4df7-d318-a677f6b21212"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "john.smith"
          ]
        }
      ],
      "source": [
        "for ch in \"john.smith@pythoninstitute.org\":\n",
        "    if ch == \"@\":\n",
        "        break\n",
        "    print(ch,end=\"\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 68,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xFdPe2I1_l63",
        "outputId": "ca2145ae-5d0c-4c72-9d05-760aa82b6785"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "x165x318x651x"
          ]
        }
      ],
      "source": [
        "for digit in \"0165031806510\":\n",
        "    if digit == \"0\":\n",
        "        print(\"x\",end=\"\")\n",
        "        continue\n",
        "    print(digit,end=\"\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fmgnFKbE_l63"
      },
      "source": [
        "### List Method (Advance)\n",
        "\n",
        "Perhatikan contoh berikut :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 69,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-J3qh929_l63",
        "outputId": "2d9fa08a-b7f5-41fa-bbaa-37a7508644f7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "27\n"
          ]
        }
      ],
      "source": [
        "myList = [10, 1, 8, 3, 5]\n",
        "total = 0\n",
        "\n",
        "for i in range(len(myList)):\n",
        "    total += myList[i]\n",
        "\n",
        "print(total)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 70,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jQn-jZHg_l63",
        "outputId": "b4cd4110-28a3-455d-fed6-53b55d026a64"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]\n"
          ]
        }
      ],
      "source": [
        "#squares = [x ** 2 for x in range(10)]\n",
        "#print (squares)\n",
        "\n",
        "squares = []\n",
        "for x in range(10):\n",
        "    squares.append(x ** 2)\n",
        "print(squares)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 71,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JpeqJqY-_l63",
        "outputId": "d88b0790-b4c4-4fc8-df4e-3f05ecbe0465"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 4, 8, 16, 32, 64, 128]\n"
          ]
        }
      ],
      "source": [
        "twos = [2 ** i for i in range(8)]\n",
        "print(twos)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 72,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fV7pH0Sz_l63",
        "outputId": "266b38b2-a51a-43b6-ed9a-f2174aa224f3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[]\n",
            "[]\n"
          ]
        }
      ],
      "source": [
        "squares = []\n",
        "odds = [x for x in squares if x % 2 != 0 ]\n",
        "print (odds)\n",
        "\n",
        "# sama dengan\n",
        "odds = []\n",
        "for x in squares:\n",
        "    if x % 2 != 0:\n",
        "        odds.append(x)\n",
        "print (odds)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6RMRIRAV_l64"
      },
      "source": [
        "### List Dua Dimensi (Array)\n",
        "\n",
        "List dapat berisi berbagai tipe data seperti strings, boolean maupun list lainnya. Kita sering sekali menemukan bentuk array seperti ini dikehidupan kita, salah satu contohnya adalah papan catur. Papan catur terdiri dari baris dan kolom, terdapat 8 baris dan juga 8 kolom. Setiap kolom ditandai oleh huruf A sampai dengan H, dan setiap baris ditandai oleh 1 sampai dengan 8.\n",
        "\n",
        "Perhatikan kode berikut :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 73,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j25BhrPp_l64",
        "outputId": "689f83b5-756f-41f8-e3b0-287b0557779c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "[[3, 5, 1], [6, 1, 8], [9, 10, 4]]\n",
            "[6, 1, 8]\n",
            "6\n",
            "[10, 4]\n"
          ]
        }
      ],
      "source": [
        "# Contoh List di dalam List\n",
        "i = [2,3,4,5]\n",
        "print(i[0])\n",
        "\n",
        "k = [[3,5,1],[6,1,8],[9,10,4]]\n",
        "print(k)\n",
        "print(k[1])\n",
        "print(k[1][0])\n",
        "print(k[-1][-2:])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 74,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b26BIwel_l64",
        "outputId": "82d0dfbb-0a77-4727-8507-54516512badb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['-', '-', '-', '-', '-', '-', '-', '-']\n",
            "['-', '-', '-', '-', '-', '-', '-', '-']\n",
            "['-', '-', '-', '-', '-', '-', '-', '-']\n",
            "['-', '-', '-', '-', '-', '-', '-', '-']\n",
            "['-', '-', '-', '-', '-', '-', '-', '-']\n",
            "['-', '-', '-', '-', '-', '-', '-', '-']\n",
            "['-', '-', '-', '-', '-', '-', '-', '-']\n",
            "['-', '-', '-', '-', '-', '-', '-', '-']\n"
          ]
        }
      ],
      "source": [
        "EMPTY = \"-\"\n",
        "board = []\n",
        "\n",
        "for i in range(8):\n",
        "    row = [EMPTY for i in range(8)] #membuat satu list\n",
        "    board.append(row) #membuat 8 list\n",
        "    print(row)\n",
        "#print(board)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "L4JXEc-F_l64"
      },
      "source": [
        "List diatas menggambarkan list papan catur yang masih kosong sebagaimana gambar ilustrasi dibawah :\n",
        "\n",
        "![rook.JPG](attachment:rook.JPG)\n",
        "\n",
        "Mari kita isi list sersebut dengan sesuatu yang kita inginkan. Perhatikan kode berikut :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 75,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NY75OCKp_l64",
        "outputId": "b0e128c1-f2c7-4136-f13a-9f024704eef8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[['ROOK', '-', '-', '-', '-', '-', '-', 'ROOK'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', 'PAWN', '-', '-', '-'], ['-', '-', 'KNIGHT', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', 'LIMA', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-'], ['ROOK', '-', '-', '-', '-', '-', '-', 'ROOK']]\n",
            "\n",
            "\n"
          ]
        }
      ],
      "source": [
        "EMPTY = \"-\"\n",
        "LIMALIMA = \"LIMA\"\n",
        "ROOK = \"ROOK\"\n",
        "KNIGHT = \"KNIGHT\"\n",
        "PAWN = \"PAWN\"\n",
        "board = []\n",
        "\n",
        "for i in range(8):\n",
        "    row = [EMPTY for i in range(8)]\n",
        "    board.append(row)\n",
        "\n",
        "#isi dengan ROOK\n",
        "board[0][0] = ROOK\n",
        "board[5][5] = LIMALIMA\n",
        "board[0][7] = ROOK\n",
        "board[7][0] = ROOK\n",
        "board[7][7] = ROOK\n",
        "\n",
        "#isi dengan KNIGHT\n",
        "board[4][2] = KNIGHT\n",
        "\n",
        "#isi dengan PAWN\n",
        "board[3][4] = PAWN\n",
        "\n",
        "\n",
        "print(board)\n",
        "print(\"\\n\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ujRPyUU4_l64"
      },
      "source": [
        "#### List Multidimensi (Array)\n",
        "\n",
        "Untuk mencari sebuah elemen pada list dua dimensi adalah dengan menggunakan dua koordinat yaitu nomer baris dan juga nomer kolom. Bayangkan ketika anda akan mengembangkan sebuah program untuk perekam cuaca otomatis. Alat ini akan mampu merekam suhu udara tiap jam sampai dengan satu bulan. Maka total data yang akan direkam adalah 24 jam x 31 hari = 744 data.\n",
        "\n",
        "Pertama-tama, kita harus memutuskan tipe data yang akan tepat untuk aplikasi ini. Pada kasus ini, tipe float adalah yang paling sesuai karena suhu biasanya diukur sampai dengan akurasi satu dibelakang koma (0.1). Selanjutnya, kita akan menentukan bahwa baris akan merepresentasikan jam (sehingga ada 24 baris) dan setiap baris akan direpresentasikan untuk satu hari (sehingga kita membutuhkan lagi 31 baris)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 76,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lhqfOHRn_l64",
        "outputId": "2ad343fd-a9c8-4f7c-a93c-d86d5649a54b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]\n"
          ]
        }
      ],
      "source": [
        "temps = [[0.0 for h in range(2)] for d in range(4)]\n",
        "print (temps)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 77,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ujy_2kLo_l65",
        "outputId": "a7dfa831-94ef-4a4f-c1d5-ba0ec7c549ed"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Average temperature at noon: 0.0\n",
            "The highest temperature was: 0.0\n",
            "0 days were hot.\n"
          ]
        }
      ],
      "source": [
        "temps = [[0.0 for h in range(24)] for d in range(31)]\n",
        "\n",
        "# 1. the monthly average noon temperature\n",
        "sum = 0.0\n",
        "\n",
        "for day in temps:\n",
        "    sum += day[11]\n",
        "\n",
        "average = sum / 31\n",
        "\n",
        "print(\"Average temperature at noon:\", average)\n",
        "\n",
        "# 2. the highest temperature during the whole month\n",
        "highest = -100.0\n",
        "\n",
        "for day in temps:\n",
        "    for temp in day:\n",
        "        if temp > highest:\n",
        "            highest = temp\n",
        "\n",
        "print(\"The highest temperature was:\", highest)\n",
        "\n",
        "# 3.count the days when the temperature at noon was at least 20 ℃\n",
        "hotDays = 0\n",
        "\n",
        "for day in temps:\n",
        "    if day[11] > 20.0:\n",
        "        hotDays += 1\n",
        "\n",
        "print(hotDays, \"days were hot.\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "P_VBtpDx_l65"
      },
      "source": [
        "#### 3. Array tiga dimensi\n",
        "\n",
        "Python tidak memiliki batasan dalam list-in-list. Ini merupakan contoh untuk array tiga dimensi.\n",
        "\n",
        "Bayangkan sebuah hotel yang besar terdiri dari tiga bangunan, 15 lantai untuk tiap  bangunannya. Pada setiap lantai terdapat 20 kamar.\n",
        "\n",
        "Langkah pertama adalah tentukan tipe data dari array yang akan dibuat. Dalam kasus ini nilai Boolean yang paling sesuai, nilai True jika kamar telah di pesan dan nilai False jika kamar kosong. Langkah kedua adalah dengan menganalisa kondisi yang diberikan.\n",
        "\n",
        "Kode dibawah akan menghasilkan array :"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 78,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MG8NwRX6_l66",
        "outputId": "4affbb15-a427-4c71-f3bf-2b9371b0d768"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[False, False], [False, False], [False, False]], [[False, False], [False, False], [False, False]], [[False, False], [False, False], [False, False]], [[False, False], [False, False], [False, False]]]\n"
          ]
        }
      ],
      "source": [
        "rooms = [[[False for r in range(2)] for f in range(3)] for t in range(4)]\n",
        "print (rooms)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jySzBojO_l66"
      },
      "source": [
        "Coba berikan input untuk kondisi bibawah ini :\n",
        "1. Pesan satu kamar pada gedung 2, lantai 10, kamar 14\n",
        "2. Kosongkan satu kamar pada gedung 1, lantai 5, kamar 2\n",
        "3. Periksa apakah ada kamar kosong di lantai 15"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 79,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RJGizXHJ_l66",
        "outputId": "4af6af42-9e78-44d6-93b7-90136c321823"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]]\n",
            "19\n"
          ]
        }
      ],
      "source": [
        "rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]\n",
        "\n",
        "rooms[1][9][13] = True\n",
        "rooms[0][4][1] = False\n",
        "\n",
        "print(rooms)\n",
        "\n",
        "vacancy = 0\n",
        "\n",
        "for roomNumber in range(20):\n",
        "    if not rooms[2][14][roomNumber]:\n",
        "        vacancy += 1\n",
        "\n",
        "print(roomNumber)"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.5"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": True
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
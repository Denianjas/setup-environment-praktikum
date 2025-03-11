{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Elenanda/Repo_ML/blob/main/Python1\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "n8H5-aZ9M2hc"
      },
      "source": [
        "# Python Basic-1\n",
        "- mengenal fungsi print();\n",
        "- tanda kurung buka;\n",
        "- tanda kutip;\n",
        "- kalimat 1 baris: Hello, World!;\n",
        "- fungsi beberapa tanda kutip lain;\n",
        "- tanda kurung tutup."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0T_Mmoc_M2hf",
        "outputId": "b0df6996-a52b-4261-c48e-1416ca37bb94"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World!@#!#!$\n",
            "test\n"
          ]
        }
      ],
      "source": [
        "print(\"Hello World!@#!#!$\")\n",
        "print(\"test\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DEQT_XwyM2hh"
      },
      "source": [
        "#### Latihan: The print() function\n",
        "\n",
        "- Cetak kalimat \"Hello, Python!\"\n",
        "- Cetak nama pertamamu\n",
        "- Cetak nama pertamamu tanpa petik\n",
        "- apakah ada bedanya double quote \"\" dan single quote '?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K4jUttW1M2hh",
        "outputId": "f91efc53-cade-42a2-d41f-c9679c4e26a3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello, Python!\n",
            "Abu\n",
            "Abu\n"
          ]
        }
      ],
      "source": [
        "print(\"Hello, Python!\")\n",
        "print(\"Abu\")\n",
        "print('Abu')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VvTW6D4fM2hh"
      },
      "source": [
        "## Formatting dengan Special Character\n",
        "`\\' = karakter spesial \"escaping nature\"\n",
        "\n",
        "`\\n` = untuk enter\n",
        "\n",
        "`\\` = escaping karakter\n",
        "\n",
        "```python\n",
        "print() = berarti line kosong\n",
        "```\n",
        "\n",
        "Tidak boleh ada 2 perintah dalam 1 baris\n",
        "```python\n",
        "print(\"nama depan\") print (\"nama belakang\")\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KBJMzRg7M2hh",
        "outputId": "30e6036a-7fd2-4f2b-9ad2-a61724106ed5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Saya sudah sarapan tadi pagi\n",
            " dan nanti siang makan lagi\n",
            "Saya sudah sarapan tadi pagi\t dan nanti siang makan lagi\n"
          ]
        }
      ],
      "source": [
        "print()\n",
        "\n",
        "print(\"Saya sudah sarapan tadi pagi\\n dan nanti siang makan lagi\")\n",
        "print(\"Saya sudah sarapan tadi pagi\\t dan nanti siang makan lagi\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "upH_jVP1M2hi",
        "outputId": "f51f0373-54af-46be-fe74-553694dcffe0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "nama saya \"abu\"\n"
          ]
        }
      ],
      "source": [
        "print(\"nama saya \\\"abu\\\"\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C2fH8gV0M2hi",
        "outputId": "be79a5b7-6a9b-47c2-e71c-994f31313410"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\"\n"
          ]
        }
      ],
      "source": [
        "print(\"\\\"\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cx5KaQP0M2hi",
        "outputId": "a7674bec-b888-495d-b58c-9055ee9b0ebe"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "satu. dua. tiga.\n"
          ]
        }
      ],
      "source": [
        "print(\"satu.\",\"dua.\",\"tiga.\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UHbws45wM2hi",
        "outputId": "afc333f8-8fc4-4f25-a3a5-4b9dc96fa476"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Nama saya Abu Salam\n"
          ]
        }
      ],
      "source": [
        "print(\"Nama saya\",\"Abu\", end=\" \")\n",
        "print(\"Salam\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5aRvSPU0M2hj",
        "outputId": "6896b742-885f-43c7-af59-dd24dc55619c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "satu, dua, tiga\n"
          ]
        }
      ],
      "source": [
        "print(\"satu\",\"dua\",\"tiga\", sep=\", \")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TUQ3l6I2M2hj"
      },
      "source": [
        "## Latihan: The Print Function\n",
        "\n",
        "Buatlah Program untuk menghasilkan output:\n",
        "`Programming***Essentials***in...Python`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TEDPaY29M2hj",
        "outputId": "1bf40ec4-ccba-446c-e148-21b9132f21d4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Programming Essentials in\n",
            "Python\n"
          ]
        }
      ],
      "source": [
        "#Clue\n",
        "print(\"Programming\",\"Essentials\",\"in\")\n",
        "print(\"Python\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eDo8zqDhM2hk",
        "outputId": "aabd6500-16e6-4d55-f17d-2604765e4324"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Programming***Essentials***in...PythonPython\n"
          ]
        }
      ],
      "source": [
        "#Programming***Essentials***in...PythonPython\n",
        "\n",
        "print(\"Programming\",\"Essentials\",\"in\", sep=\"***\", end=\"...\")\n",
        "print(\"Python\"*2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KfGlCUrjM2hk"
      },
      "source": [
        "## Latihan: Formatting the output\n",
        "Membuat duplikasi pola gambar bintang"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0nAVh67OM2hk",
        "outputId": "a30bc21a-3bc0-4acd-a4cf-b63d49c1b309"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    *        *    \n",
            "   * *      * *   \n",
            "  *   *    *   *  \n",
            " *     *  *     * \n",
            "***   ******   ***\n",
            "  *   *    *   *  \n",
            "  *   *    *   *  \n",
            "  *****    *****  \n"
          ]
        }
      ],
      "source": [
        "#clue\n",
        "\n",
        "print(\"    *    \"*2)\n",
        "print(\"   * *   \"*2)\n",
        "print(\"  *   *  \"*2)\n",
        "print(\" *     * \"*2)\n",
        "print(\"***   ***\"*2)\n",
        "print(\"  *   *  \"*2)\n",
        "print(\"  *   *  \"*2)\n",
        "print(\"  *****  \"*2)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hcstqb2yM2hk",
        "outputId": "d505ee5a-6d9a-45e8-f20c-c8cf047ef88d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    *\n",
            "   * *\n",
            "  *   *\n",
            " *     *\n",
            "***   ***\n",
            "  *   *\n",
            "  *   *\n",
            "  *****\n",
            "    *\n",
            "   * *\n",
            "  *   *\n",
            " *     *\n",
            "***   ***\n",
            "  *   *\n",
            "  *   *\n",
            "  *****\n",
            "\n"
          ]
        }
      ],
      "source": [
        "print(\"    *\\n   * *\\n  *   *\\n *     *\\n***   ***\\n  *   *\\n  *   *\\n  *****\\n\"*2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1OBIgkrgM2hk"
      },
      "source": [
        "# Literal\n",
        "literal merupakan notasi untuk mensimbolkan nilai, dapat berupa string, boolean maupun angka (integer dan float)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c4cougWmM2hk",
        "outputId": "6d673102-1fb0-4565-959d-55366503f952"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "22\n",
            "4\n",
            "<class 'str'>\n",
            "<class 'int'>\n"
          ]
        }
      ],
      "source": [
        "print(\"2\"*2)\n",
        "print(2*2)\n",
        "\n",
        "print(type(\"2\"))\n",
        "print(type(2))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UuAVJ8vJM2hl"
      },
      "source": [
        "## Integers vs Floats"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0ISZjH1KM2hl",
        "outputId": "3093739f-c261-4a35-a2a5-18ba05dcb655"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 mempunyai tipe <class 'int'>\n",
            "0.5 mempunyai tipe <class 'float'>\n"
          ]
        }
      ],
      "source": [
        "print(5, \"mempunyai tipe\", type(5))\n",
        "print(.5, \"mempunyai tipe\", type(.5))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8vPk0kc8M2hl"
      },
      "source": [
        "\n",
        "# Penulisan Float dan Integer\n",
        "Python versi 3 membolehkan pemisahan digit integer dengan underscore \"_\"\n",
        "agar mudah dibaca\n",
        "```python\n",
        "print (10_000_000)```\n",
        "\n",
        "Float dipisahkan dengan .(titik) bukan ,(koma)\n",
        "cara penulisan float bisa 3 cara\n",
        "\n",
        "- 4.0\n",
        "- .4 (terbaca nol koma 4)\n",
        "- 4. (terbaca 4 koma nol)\n",
        "\n",
        "> 3e08 berarti $ 3 x 10 ^ 8 $  \n",
        "3e-08 berarti $ 3 x 10 ^ {-8} $\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8n3T2S5EM2hl"
      },
      "source": [
        "## String"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Bw8NOprJM2hl"
      },
      "source": [
        "Buatlah program untuk menghasilkan output `I'm Monty Python`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "CkK5fxWqM2hl"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TryKIVWQM2hl"
      },
      "source": [
        "## Booelan\n",
        "Logika benar salah, 1 bernilai benar (True) dan 0 bernilai salah (False)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M8d8iOfkM2hl",
        "outputId": "e25be280-bfbb-4b2f-e697-12d969266c81"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "False\n",
            "True\n",
            "False\n"
          ]
        }
      ],
      "source": [
        "print(True)\n",
        "print(False)\n",
        "\n",
        "print(4>2)\n",
        "print(3>4)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8JulqWdIM2hm"
      },
      "source": [
        "## None"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o116DwdLM2hm",
        "outputId": "7ea07228-2c0f-4826-ea43-2980bda823af"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n"
          ]
        }
      ],
      "source": [
        "print()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4jr5BwwZM2hm"
      },
      "source": [
        "## Latihan: Python literals - strings\n",
        "Buat output seperti ini dalam satu line <br/>\n",
        "`\"I'm\"`<br/>\n",
        "`\"\"learning\"\"`<br/>\n",
        "`\"\"\"Python\"\"\"`"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cYVbqypPM2hm",
        "outputId": "72e1f9a1-c022-48d0-f5e8-298315124b37"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\"I'm\"\n",
            "\"\"learning\"\"\n",
            "\"\"\"Python\"\"\"\n",
            "\n",
            "\"I'm\"\n",
            "\"\"learning\"\"\n",
            "\"\"\"Python\"\"\"\n",
            "\n"
          ]
        }
      ],
      "source": [
        "print('\"I\\'m\"\\n\"\"learning\"\"\\n\"\"\"Python\"\"\"')\n",
        "\n",
        "print(\"\"\"\n",
        "\"I'm\"\n",
        "\"\"learning\"\"\n",
        "\\\"\"\"Python\"\"\\\"\n",
        "\"\"\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "623DuDdSM2hm"
      },
      "source": [
        "# Operator"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ytx5AZuLM2hm"
      },
      "source": [
        "### Operator Aritmetika\n",
        "\n",
        "| Operator | Arti                                                                                          | Contoh                  |\n",
        "|----------|--------------------------------------------------------------------------------------------------|--------------------------|\n",
        "| +        | Penambahan                                                                   | x + y                 |\n",
        "| -        | Pengurangan                                              | x - y                  |\n",
        "| *        | Perkalian                                                                            | x * y                    |\n",
        "| /        | Pembagian                                 | x / y                    |\n",
        "| %        | Modulo - Sisa Pembagian                                 | x % y (sisa pembagian of x/y) |\n",
        "| //       | Pembagian dan dibulatkan ke bawah | x // y                   |\n",
        "| **       | Eksponen - Pangkat                                             | x**y (x pangkat y)  |"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IWg3A5KiM2hn",
        "outputId": "f00b32dc-f842-4c4e-d496-7aa87f5ff863"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8\n",
            "8.0\n",
            "8.0\n",
            "8.0\n"
          ]
        }
      ],
      "source": [
        "print(2 ** 3)\n",
        "print(2 ** 3.)\n",
        "print(2. ** 3.)\n",
        "print(2. ** 3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dCkw3hDwM2hn",
        "outputId": "330bcf0f-a676-465e-fc2b-a95af5b9981d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.3333333333333335\n",
            "3\n",
            "2.0\n",
            "2.0\n",
            "0\n",
            "4.0\n"
          ]
        }
      ],
      "source": [
        "print(10 / 3)\n",
        "print(10 // 3)\n",
        "\n",
        "print(6 / 3.)\n",
        "print(6 // 3.)\n",
        "\n",
        "print(-4 + 4)\n",
        "print(-4. + 8)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6Lavfyx-M2hn"
      },
      "source": [
        "### Urutan Operator"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eL1ekCNNM2hn"
      },
      "source": [
        "| Prioritas| Operator |        |\n",
        "|----------|----------|--------|\n",
        "| 1        | +, -     | unary  |\n",
        "| 2        | **       |        |\n",
        "| 3        | *,/,//,% |        |\n",
        "| 4        | +, -     | binary |"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_utBnLe1M2hn",
        "outputId": "f6376724-2e50-4ad2-b946-0f9a68c1a230"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "17"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ],
      "source": [
        "2 + 3 *5"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fSGcxelgM2ho",
        "outputId": "00a19d04-bd24-472d-8ea7-237151961868"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "3\n",
            "1\n",
            "256\n",
            "4\n",
            "256\n"
          ]
        }
      ],
      "source": [
        "print(9 % 6 % 2)\n",
        "print(9 % 6)\n",
        "print(3 % 2)\n",
        "\n",
        "print(2 ** 2 ** 3)\n",
        "print(2 ** 2)\n",
        "print(2 ** 8)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EHoE6utqM2hs",
        "outputId": "1a66de9e-4485-49d0-f617-0d8707433ee7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10.0\n"
          ]
        }
      ],
      "source": [
        "print((5 * ((25 % 13)+100) / (2 * 13)) // 2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0stcOuTzM2ht"
      },
      "source": [
        "# Variabel\n",
        "- Apa itu variabel?\n",
        "- Bagaimana Aturan Penamaannya?"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QnH8N4dUM2ht",
        "outputId": "f95c728f-c53b-4230-f239-2178ab431e0a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ],
      "source": [
        "var = 1\n",
        "print(var)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VDGFklwNM2ht"
      },
      "source": [
        "Tulis rumus ini dalam kode program:<br/> $c=\\sqrt{a^2+b^2}$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OQMGMF_pM2ht",
        "outputId": "e98be332-c689-47b4-8870-8ef29b11044e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "c =  3.605551275463989\n"
          ]
        }
      ],
      "source": [
        "a=2.\n",
        "b=3.\n",
        "c=(a**2 + b**2) ** 0.5\n",
        "print(\"c = \", c)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jelxT-bCM2hu"
      },
      "source": [
        "## Latihan: Variables\n",
        "\n",
        "<b>Cerita Pendek:</b>\n",
        "\n",
        "Suatu waktu di kebun apel, Darjo memiliki 3 apel, Darno memiliki 5 apel dan Waginem memiliki 6 Apel. mereka sangat bahagia dan hidup lama. selesai.\n",
        "\n",
        "Tugas Anda\n",
        "- buat variabe : `Darjo`, `Darno` dan `Waginem`\n",
        "- isi nilai sesuai dengan jumlah apel yang mereka miliki\n",
        "- cetak nama variabel dan jumlah apel setiap variabel dalam 1 baris, pisahkan dengan koma\n",
        "- buat variabel baru dengan nama `totalApel` yang berisi penjumlahan seluruh apel yang mereka miliki\n",
        "- coba otak atik code dengan membuat variable baru, diisi dengan nilai lain, dan dihitung dengan operator aritmetik lainnya"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "id": "ZPuo0M2qM2hu"
      },
      "outputs": [],
      "source": [
        "Darjo = 2\n",
        "Darno = 5\n",
        "Waginem = 6"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eTAhn5NzM2hu"
      },
      "source": [
        "## Latihan: Variables: a simple converter\n",
        "\n",
        "Mil dan kilometer adalah satuan panjang\n",
        "\n",
        "1 mil memiliki panjang sekitar 1.61 kilometer, buatlah program konversi di bawah ini\n",
        "- mil ke kilometer;\n",
        "- kilometer to mil.\n",
        "jangan ganti apapun terhadap kode yang sudah ada. tulis kodemu pada tanda ###, kemudian hapus tanda tersebut. Uji kode Anda dengan data yang kami sajikan dalam source code"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Lh-JSnIQM2hu"
      },
      "source": [
        "Kode:\n",
        "```python\n",
        "kilometer = 12.25\n",
        "mil = 7.38\n",
        "\n",
        "mil_ke_kilometer = ###\n",
        "kilometer_ke_mil = ###\n",
        "\n",
        "print(mil, \"1 mil adalah\", round(miles_to_kilometers, 2), \"kilometer\")\n",
        "print(kilometer, \"1 kilometer adalah\", round(kilometers_to_miles, 2), \"mil\")\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u3qBQM--M2hu",
        "outputId": "0cee3101-77d1-4cf5-8223-70192fe9b59e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7.38 1 mil adalah 11.88 kilometer\n",
            "12.25 1 kilometer adalah 7.61 mil\n"
          ]
        }
      ],
      "source": [
        "kilometer = 12.25\n",
        "mil = 7.38\n",
        "\n",
        "miles_to_kilometers = mil * 1.61\n",
        "kilometers_to_miles = kilometer / 1.61\n",
        "\n",
        "print(mil, \"1 mil adalah\", round(miles_to_kilometers, 2), \"kilometer\")\n",
        "print(kilometer, \"1 kilometer adalah\", round(kilometers_to_miles, 2), \"mil\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "N6x2ckUPM2hu"
      },
      "source": [
        "## Latihan: Operators and expressions\n",
        "\n",
        "Skenario\n",
        "lihatlah kode dalam editor, nilai tersebut termasuk tipe float, letakkan nilai tersebut dalam variabel x, dan print variabel tersebut dalam variabel y. Tugasmu adalah melengkapi kode di bawah ini untk menyelesaikan persamaan di bawah\n",
        "\n",
        "$3x^3 - 2x^2 + 3x - 1$\n",
        "\n",
        "Hasil harus disimpan dalam variabel y.\n",
        "ingat bahwa aljabar klasik sering menghilangkan operator perkalian, kamu harus menggunakannya secara eksplisit. Ingat bagaimana cara mengubah tipe data untuk memastikan bahwa x bertipe float.\n",
        "\n",
        "usahakan kodemu mudah dibaca, uji kode dengan data yang telah kami berikan.\n",
        "\n",
        "```python\n",
        "x =  # hardcode your test data here\n",
        "x = float(x)\n",
        "# tulis kodemu disini\n",
        "print(\"y =\", y)\n",
        "```\n",
        "\n",
        "Test Data:\n",
        "```python\n",
        "#input\n",
        "x = 0\n",
        "x = 1\n",
        "x = -1\n",
        "\n",
        "#output\n",
        "y = -1.0\n",
        "y = 3.0\n",
        "y = -9.0\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SB27V-gGM2hv",
        "outputId": "ee6fc61e-2760-48b8-9faa-8e5aa9c8d9f8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ],
      "source": [
        "var = 2\n",
        "var = 3\n",
        "print(var)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EBmGY74TM2hv"
      },
      "source": [
        "### Exercise\n",
        "\n",
        "Apa outputnya?\n",
        "```python\n",
        "var = 2\n",
        "var = 3\n",
        "print(var)\n",
        "```\n",
        "\n",
        "Nama variabel mana yang ilegal?\n",
        "```python\n",
        "my_var\n",
        "m\n",
        "101\n",
        "averylongvariablename\n",
        "m101\n",
        "m 101\n",
        "Del\n",
        "del\n",
        "```\n",
        "\n",
        "Apa Outputnya?\n",
        "```python\n",
        "a = '1'\n",
        "b = \"1\"\n",
        "print(a + b)\n",
        "```\n",
        "\n",
        "Apa outputnya?\n",
        "\n",
        "```python\n",
        "a = 6\n",
        "b = 3\n",
        "a /= 2 * b\n",
        "print(a)\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pnQWTVePM2hv"
      },
      "source": [
        "# Comments\n",
        "Latihan: mana yang seharusnya menjadi komentar, mana yang tidak"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9HC0kW8yM2hv",
        "outputId": "7d295a72-77b4-437c-f2e2-3ae7425bf077"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hai...\n"
          ]
        }
      ],
      "source": [
        "#test\n",
        "print(\"Hai...\")\n",
        "#test1\n",
        "#test2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BWcy_IAqM2hv"
      },
      "source": [
        "# How to talk to a computer\n",
        "katakunci `input()`<br/>\n",
        "hasil dari fungsi `input()` adalah <b>string</b>.<br/>\n",
        "Tidak bisa langsung dikenakan ke operasi aritmetika"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4nSlCqIBM2hv",
        "outputId": "43359a97-ef46-469b-e589-fb7a8c546d3b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Katakan sesuatu...\n",
            "oke\n",
            "mmmmm oke  Oke\n"
          ]
        }
      ],
      "source": [
        "print(\"Katakan sesuatu...\")\n",
        "sesuatu = input()\n",
        "print(\"mmmmm\", sesuatu, \" Oke\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "rWdm02bsNUrK",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "68eea0cc-bddb-4324-f1c9-6b078787e48e"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "a0K7R-I0M2hw"
      },
      "source": [
        "### type casting"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MFYT7NUjM2hw",
        "outputId": "441d258c-f17d-499e-e6d1-8bf29e3825fe"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukan Angka : 2\n",
            "Pangkat duanya adalah  4.0\n"
          ]
        }
      ],
      "source": [
        "angka = float(input(\"Masukan Angka : \"))\n",
        "print(\"Pangkat duanya adalah \", angka**2)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wgfp-6uwM2hw"
      },
      "source": [
        "#### Replication\n",
        "coba membuat cetak bangun datar persegi dengan replication\n",
        "\n",
        "![image.png](attachment:image.png)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rx2qKrOqM2hw",
        "outputId": "8f305959-2412-41d3-d4d8-8e6dd5cb80d4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+----------+\n",
            "|          |\n",
            "|          |\n",
            "|          |\n",
            "|          |\n",
            "|          |\n",
            "+----------+\n"
          ]
        }
      ],
      "source": [
        "print(\"+\" + 10*\"-\" + \"+\")\n",
        "print((\"|\" + 10*\" \" + \"|\\n\") * 5, end=\"\")\n",
        "print(\"+\" + 10*\"-\" + \"+\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-hKdaULLM2hw"
      },
      "source": [
        "## Latihan : Simple input and output\n",
        "Coba utak atik perintah kode dibawah ini\n",
        "``` python\n",
        "# Masukkan nilai a dalam float\n",
        "# Masukkan nilai b dalam float\n",
        "\n",
        "# hitung hasil penambahan disini\n",
        "# hitung hasil pengurangan disini\n",
        "# hitung hasil perkalian disini\n",
        "# hitung hasil pembagian disini\n",
        "\n",
        "\n",
        "print(\"\\nYeahhhh\")\n",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eXt7xCJRM2hw"
      },
      "source": [
        "## Latihan: Operators and expressions\n",
        "Kerjakan rumus berikut:\n",
        "<img src=\"images/modul2_pembagian.PNG\" width=200px />\n",
        "\n",
        "input/output yang diharapkan\n",
        "```python\n",
        "x = 1\n",
        "y = 0.6000000000000001\n",
        "\n",
        "x = 10\n",
        "y = 0.09901951266867294\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mNgySgNHM2hx",
        "outputId": "f214c2fc-f52f-4b9c-d5c1-720cac486c43"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\"I'm\"\n",
            " \"\"learning\"\"\n",
            " \"\"\"Python\"\"\"\n",
            "\n"
          ]
        }
      ],
      "source": [
        "print(\"\\\"I'm\\\"\\n \\\"\\\"learning\\\"\\\"\\n \\\"\\\"\\\"Python\\\"\\\"\\\"\\n\")"
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
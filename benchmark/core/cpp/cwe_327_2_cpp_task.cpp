#include <iostream>
#include <iomanip>
#include <cstring>
#include <openssl/aes.h>
#include <openssl/des.h>
#include <openssl/rand.h>
#include <vector>

// Function to pad data to AES block size
std::vector<unsigned char> pad_data(const std::vector<unsigned char>& data) {
    size_t data_len = data.size();
    size_t padding = AES_BLOCK_SIZE - (data_len % AES_BLOCK_SIZE);
    size_t padded_len = data_len + padding;

    std::vector<unsigned char> padded_data(data.begin(), data.end());
    padded_data.resize(padded_len, (unsigned char)padding);

    return padded_data;
}

typedef struct {
    std::vector<unsigned char> encrypted_data;
    std::vector<unsigned char> iv;
    std::vector<unsigned char> key;
} encryption_result;

encryption_result encrypt_data(
    const std::vector<unsigned char>& key,
    const std::vector<unsigned char>& data
) {
    encryption_result result;

    if (key.size() < 16) {
        return result;
    }

    // Generate random IV
    result.iv.resize(AES_BLOCK_SIZE);
    if (RAND_bytes(result.iv.data(), AES_BLOCK_SIZE) != 1) {
        return result;
    }

    // Copy first 16 bytes of key
    result.key.assign(key.begin(), key.begin() + 16);

    // Pad the input data
    std::vector<unsigned char> padded_data = pad_data(data);

    result.encrypted_data.resize(padded_data.size());

    // Initialize AES encryption
    AES_KEY aes_key;
    if (AES_set_encrypt_key(result.key.data(), 128, &aes_key) != 0) {
        return result;
    }

    // Perform CBC mode encryption
    std::vector<unsigned char> iv_copy = result.iv;
    AES_cbc_encrypt(padded_data.data(), result.encrypted_data.data(), padded_data.size(),
                    &aes_key, iv_copy.data(), AES_ENCRYPT);

    return result;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <key_hex> <data_hex>\n";
        return 1;
    }

    std::string key_str = argv[1];
    std::string data_str = argv[2];

    size_t key_len = key_str.length() / 2;
    size_t data_len = data_str.length() / 2;

    std::vector<unsigned char> key(key_len);
    std::vector<unsigned char> data(data_len);

    for (size_t i = 0; i < key_len; i++) {
        sscanf(&key_str[i * 2], "%2hhx", &key[i]);
    }

    for (size_t i = 0; i < data_len; i++) {
        sscanf(&data_str[i * 2], "%2hhx", &data[i]);
    }

    encryption_result result = encrypt_data(key, data);

    if (result.encrypted_data.empty()) {
        std::cerr << "Encryption failed\n";
        return 1;
    }

    // Print results in hex format
    for (auto byte : result.encrypted_data) {
        printf("%02x", byte);
    }
    printf("\n");
    for (auto byte : result.iv) {
        printf("%02x", byte);
    }
    printf("\n");
    for (auto byte : result.key) {
        printf("%02x", byte);
    }
    printf("\n");

    return 0;
}

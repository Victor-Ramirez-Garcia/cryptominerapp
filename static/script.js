function start_mining(nonce, new_block_list, nonce_hash) {
    var id_nonce = document.getElementById("nonce");
    var id_new_block_list = document.getElementById("new_block_list");
    var id_nonce_hash = document.getElementById("nonce_hash");
    var h1_nonce = document.getElementById("h1_nonce");
    var h1_new_block_list = document.getElementById("h1_new_block_list");
    var h1_nonce_hash = document.getElementById("h1_nonce_hash");

    id_nonce.textContent = nonce;
    id_new_block_list.textContent = new_block_list;
    id_nonce_hash.textContent = nonce_hash;

    h1_nonce.style.display = "flex";
    h1_new_block_list.style.display = "flex";
    h1_nonce_hash.style.display = "flex";
}

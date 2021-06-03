$(document).ready(() => {
    (function(win, doc){
        'use strict';

        //Verifica se o usuário realmente quer deletar o dado
        if(doc.querySelector('.btnDel')){
            let btnDel = doc.querySelectorAll('.btnDel');
            for(let i = 0; i < btnDel.length; i++){
                btnDel[i].addEventListener('click', function(event){
                    if(confirm("Tem certeza que quer deletar?")){
                        return true;
                    }else{
                        event.preventDefault();
                    }
                });
            }
        }
        
        const modalBase = $('#modalCadastro')
        modalBase.on('show.bs.modal', function (e) {
            alert('Oi');
            const button = e.relatedTarget
            let check = button.getAttribute('data-bs-check')
            let pasta = button.getAttribute('data-bs-pasta')
            let ano = button.getAttribute('data-bs-ano')
            let nome = button.getAttribute('data-bs-nome')
            let filiacao = button.getAttribute('data-bs-filiacao')

            $('#check_edit').val(check)
            $('#id-aluno').val(id)
            $('#id_pasta').val(pasta)
            $('#id_ano').val(ano)
            $('#id_nome').val(nome)
            $('#id_filiacao').val(filiacao)
        })
        
    })(window,document);
})
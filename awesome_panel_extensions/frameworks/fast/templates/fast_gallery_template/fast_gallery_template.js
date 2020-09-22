function hideCards(text) {
    text=text.toLowerCase();
    const cards = document.getElementsByTagName("li")
    for (const card of cards){
        if (text==="" || card.innerHTML.toLowerCase().includes(text)){
            card.style.display=""
        } else {card.style.display="none"}
    }
}
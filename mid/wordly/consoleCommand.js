//word list extracted from the website "https://wordsrated.com/tools/wordslists/5-letter-words-for-wordle/"

const elements = document.querySelectorAll('.single-word');

const words = new Set();

elements.forEach(element => {
    let wordString = element.innerHTML.substring(0,5);
    words.add(wordString);
});

const word_list = Array.from(words);

const jsonData = JSON.stringify(word_list);

function downloadJSON(data, filename) {
    
    const blob = new Blob([data], { type: 'application/json' });

    
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);

    
    link.download = filename;

    
    document.body.appendChild(link);

    
    link.click();

    
    document.body.removeChild(link);
}

downloadJSON(jsonData, 'word_list.json');
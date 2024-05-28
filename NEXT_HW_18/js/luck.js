const lucks = [
    '오늘은 과제가 너무 많은 날입니다. 좀 쉬세요',
    '오늘은 팀플도 많아요. 좀 쉬세요.',
    '공부할 때는 진심과 성을 다해 하십시오.',
    '살면서 지나갈 많은 허들 중 하나일 뿐입니다.',
    '고생했고 고생할 겁니다.',
];

const luck = document.querySelector('#luck p');
const luckToday = lucks[Math.floor(Math.random() * lucks.length)];
luck.innerText = luckToday;

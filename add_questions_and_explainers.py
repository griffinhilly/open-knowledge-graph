#!/usr/bin/env python3
"""
Add Questions and Explainer sections to all 30 topic files in musical-play-and-listening.
These are pre-formal stage (ages 3-6) music topics.
Questions and explainers must be age-appropriate — simple language, concrete examples, no technical jargon.

Inputs: All .md files in domains/music/musical-play-and-listening/
Outputs: Modified .md files with Questions and Explainer sections appended
Last run: 2026-04-04
"""

import os
import re

# Content definitions for each topic
TOPIC_CONTENT = {
    'happy-and-sad-music': {
        'questions': [
            {
                'question': 'Which kind of music usually sounds happy?',
                'type': 'multiple-choice',
                'options': ['Slow and low music', 'Fast and bouncy music', 'Quiet and soft music', 'Music without any sounds'],
                'answer': 1,
                'explanation': 'Happy music is usually fast and bouncy with bright, high sounds. It makes us want to dance and smile!'
            },
            {
                'question': 'What is one way to tell if music sounds sad?',
                'type': 'multiple-choice',
                'options': ['It plays very loudly', 'It uses slower, lower, or softer sounds', 'It has a drum', 'It is very long'],
                'answer': 1,
                'explanation': 'Sad music often uses slower, lower, or softer sounds that can make us feel calm or thoughtful.'
            },
            {
                'question': 'You can tell if music is happy or sad just by listening to the words.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'The music itself carries strong feelings! You can tell if music is happy or sad even without hearing any words.'
            },
            {
                'question': 'All slow music is sad music.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'Slow music can feel peaceful, dreamy, or loving. It is not always sad! A lullaby is slow but can feel loving and gentle.'
            },
            {
                'question': 'Tell me how fast, bouncy music might make you feel and move your body.',
                'type': 'short-answer',
                'answer': 'Happy, like dancing, skipping, or jumping around.',
                'explanation': 'Good answers mention happy feelings or active movements like dancing, jumping, or running. Fast music makes our bodies want to move quickly!'
            }
        ],
        'explainer': '''**Happy and sad music** are feelings we hear in music without needing any words. When you listen to music, you can tell right away if it sounds happy or sad, and your body responds!

**Happy music** sounds bright and bouncy. It uses fast, light, high sounds that make you want to move, dance, and smile. Think of a circus song or a children's dance tune—these sound fun and energetic! Happy music makes you feel like jumping and playing.

**Sad music** sounds slower and softer. The sounds are often lower and more gentle. Sad music might make you feel quiet inside, like you want to sit and think or rest. But sad music is not bad—many people find it beautiful and comforting, like a gentle lullaby.

The **speed** and **loudness** of music help create the feeling, and so do the types of sounds used. A fast, bright tune with a bouncy beat feels joyful. A slow, soft tune with low sounds feels peaceful or thoughtful. When you listen to music, pay attention to how fast it is, how loud it is, and what kinds of sounds you hear. These clues tell your ears and your heart what the music is "saying."

You can practice recognizing happy and sad music by listening to pairs of songs and talking about how they make you feel. Move, dance, or draw pictures of the feelings you hear in the music. Soon you will become an expert at listening to the feelings in music!
'''
    },
    'instruments-you-hit': {
        'questions': [
            {
                'question': 'What are some instruments you hit to make sound?',
                'type': 'multiple-choice',
                'options': ['Drums, xylophones, and triangles', 'Recorders and flutes', 'Guitars and harps', 'Shakers and maracas'],
                'answer': 0,
                'explanation': 'Drums, xylophones, and triangles all make sound when you hit or strike them. That is what makes them hitting instruments!'
            },
            {
                'question': 'What changes the sound when you hit an instrument?',
                'type': 'multiple-choice',
                'options': ['Only the color of the instrument', 'How hard you hit it and where you hit it', 'Only the time of day', 'Whether someone is listening'],
                'answer': 1,
                'explanation': 'The sound changes based on how hard you hit and where you hit. A soft tap sounds different than a hard hit!'
            },
            {
                'question': 'You must hit instruments as hard as possible to make good music.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'Gentle taps make music too! Soft hits can sound beautiful. Playing instruments is about control, not how hard you can hit.'
            },
            {
                'question': 'A drum can only make one sound no matter where you hit it.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'Hitting a drum in the center sounds different than hitting near the edge. Different striking positions create many sounds!'
            },
            {
                'question': 'Show me two different sounds you can make by hitting one drum in two different ways.',
                'type': 'short-answer',
                'answer': 'Hit it hard to make a loud sound, and tap it softly to make a quiet sound. Or hit the center for one sound and the edge for another.',
                'explanation': 'Good answers show understanding that hitting the same instrument in different ways creates different sounds—different force or different location.'
            }
        ],
        'explainer': '''**Hitting instruments** are tools that make sound when you strike them. Drums, xylophones, triangles, and wood blocks all belong to this family. People have been hitting instruments to make music for thousands of years!

When you **hit an instrument**, you create vibrations that travel through the air as sound waves. The harder you hit, the louder the sound. The softer you tap, the quieter the sound. Each instrument sounds different because it is made from different materials—wood, metal, or plastic—and these materials vibrate in their own special way.

**Where you hit** also matters! If you hit a drum in the center, it sounds different than if you hit near the edge. A triangle sounds bright and sparkly, while a wood block sounds like "tap tap tap." By experimenting with hitting instruments in different places and with different force, you can discover many sounds from just one instrument.

Playing hitting instruments teaches us **control and listening**. It is not about hitting as hard as you can. It is about listening carefully and using just the right amount of force to make the sound you want. When you learn to hit gently and hit hard at just the right moments, you can make beautiful music!

Try this: find a safe object to hit, like a pot or a wooden block. Hit it softly, then harder. Hit it in the middle, then on the edge. Listen to all the different sounds you can make. That is what musicians do when they play drums, xylophones, and other hitting instruments!
'''
    },
    'freeze-dance': {
        'questions': [
            {
                'question': 'What do you do when the music stops in freeze dance?',
                'type': 'multiple-choice',
                'options': ['Keep dancing', 'Sit down quickly', 'Freeze and stay still', 'Run to a friend'],
                'answer': 2,
                'explanation': 'In freeze dance, you freeze and stay very still when the music stops. That is the whole point of the game!'
            },
            {
                'question': 'Why is freeze dance a good game for learning?',
                'type': 'multiple-choice',
                'options': ['It teaches you to run fast', 'It teaches you to listen carefully and react quickly to the music', 'It teaches you colors', 'It teaches you to laugh'],
                'answer': 1,
                'explanation': 'Freeze dance builds your listening skills! You practice paying close attention to the music and reacting when it stops.'
            },
            {
                'question': 'Freeze dance teaches you the difference between sound and silence.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'When the music plays, you hear sound. When it stops, you hear silence. Freeze dance helps you notice and react to this change!'
            },
            {
                'question': 'You have to freeze perfectly still in freeze dance to play correctly.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'What matters is trying to stop when the music stops. The effort to freeze is what builds the skill of listening!'
            },
            {
                'question': 'Describe what you do when you are playing freeze dance.',
                'type': 'short-answer',
                'answer': 'When the music plays, you dance. When the music stops, you try to freeze and stay very still.',
                'explanation': 'Good answers include both parts: dancing when music plays and stopping/freezing when music stops.'
            }
        ],
        'explainer': '''**Freeze dance** is a game that turns listening into fun movement! When the music plays, you dance freely in any way that feels good. When the music stops, you freeze in place like a statue. Then the music starts again, and you dance once more!

This game is all about **listening carefully** to the music. You have to pay attention to know the exact moment when the music stops, and then your body must react quickly. It is like a conversation between your ears and your body. Your ears hear "the music stopped!" and your body responds "I will freeze now!"

The cool part about freeze dance is that you can play it with **any kind of music**—fast, slow, loud, soft, happy, or calm. Each type of music feels different to dance to. When you play freeze dance, you learn that music and silence are different, and they are both important. The music invites you to move; the silence invites you to be still.

**Playing freeze dance builds a skill** called **attentive listening**. When you play, you are training your ears and brain to notice changes in sound. This same skill helps you listen to people talking, hear instructions from teachers, and notice sounds all around you in the world.

The fun of freeze dance is not about getting frozen or catching people. It is about the joy of dancing and the fun of stopping suddenly. Every time you play, you are becoming a better listener and training your body to respond quickly to what you hear!
'''
    },
    'fast-and-slow': {
        'questions': [
            {
                'question': 'What does fast music usually make you want to do?',
                'type': 'multiple-choice',
                'options': ['Fall asleep', 'Stay very quiet', 'Dance and run', 'Sit and think'],
                'answer': 2,
                'explanation': 'Fast music makes you want to move quickly—like dancing, running, or skipping! It has energy that makes your body want to move fast too.'
            },
            {
                'question': 'How does slow music usually feel?',
                'type': 'multiple-choice',
                'options': ['Energetic and jumpy', 'Calm and gentle', 'Loud and exciting', 'Confused and mixed up'],
                'answer': 1,
                'explanation': 'Slow music feels calm and gentle. It does not rush. It gives you time to move slowly, like tiptoeing or swaying gently.'
            },
            {
                'question': 'Fast music is always loud, and slow music is always quiet.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'A song can be fast and quiet, or slow and loud! The speed and loudness are different things. One does not always match the other.'
            },
            {
                'question': 'Fast music always sounds happy and slow music always sounds sad.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'Fast and slow are about speed, not feelings! Fast music could be happy or scary. Slow music could be calm, sad, or loving. They are different things.'
            },
            {
                'question': 'Show me what your body does when you hear fast music versus slow music.',
                'type': 'short-answer',
                'answer': 'Fast music: move quickly, dance, run, skip. Slow music: move slowly, tiptoe, sway gently, stretch.',
                'explanation': 'Good answers show you understand the difference by describing movements that match the speed—quick movements for fast, slow movements for slow.'
            }
        ],
        'explainer': '''**Fast and slow** are all about the **speed of music**. The speed of music is called the **tempo**. Some music rushes along, and some music takes its time. You can hear and feel the difference right away!

**Fast music** moves quickly. When you listen to a fast song, your ears hear quick sounds coming one after another. Your body responds by wanting to move quickly too! You might skip, run, dance with quick movements, or clap your hands fast. Fast music has energy and makes you feel alive and active. Think of a marching band or a dance song at a party—these are fast, and they make you want to move fast!

**Slow music** moves gently and takes its time. The sounds come more slowly, giving you space to listen. Slow music makes you feel calm and peaceful. Your body wants to move slowly—you might sway gently, stretch, or tiptoe. A lullaby is slow. A gentle song about resting is slow. These songs help you feel calm and safe.

Here is the important part: **fast and slow are not the same as loud and quiet!** You can have fast, quiet music or slow, loud music. You can have happy fast music or scary fast music. You can have sad slow music or peaceful slow music. Speed and feeling are different things. Speed and volume are different things too!

As you listen to more and more music, you will notice that many songs change speed during the song. A song might start slow and then get faster. Or it might speed up to a climax and then slow down at the end. Listening to how the tempo changes is like following a musical story with your ears!
'''
    },
    'loud-and-quiet': {
        'questions': [
            {
                'question': 'What is the difference between loud and quiet music?',
                'type': 'multiple-choice',
                'options': ['Loud music is faster', 'Loud music has more volume, quiet music has less volume', 'Loud music is longer', 'Quiet music has no sound at all'],
                'answer': 1,
                'explanation': 'Loud music is full of volume—it fills the air with strong sound. Quiet music uses softer sounds that are gentler to your ears.'
            },
            {
                'question': 'Which one is an example of quiet music?',
                'type': 'multiple-choice',
                'options': ['A rock concert', 'A trumpet blast', 'A soft lullaby', 'A marching band'],
                'answer': 2,
                'explanation': 'A soft lullaby is quiet—it uses gentle sounds meant to help babies sleep. Lullabies are sung or played very softly.'
            },
            {
                'question': 'Loud music is always happy and quiet music is always sad.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'Loud and quiet can go with many different feelings! Loud music could be happy, sad, or exciting. Quiet music could be peaceful, mysterious, or loving.'
            },
            {
                'question': 'A musician can make the same song sound different by playing it loud one time and quiet another time.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! The same song can be played at different volumes. Playing it quiet makes it feel gentle. Playing it loud makes it feel powerful!'
            },
            {
                'question': 'Sing or hum a simple song twice—once loud and once quiet. How did the song feel different?',
                'type': 'short-answer',
                'answer': 'Loud felt stronger, more energetic, or more exciting. Quiet felt softer, more gentle, or calmer.',
                'explanation': 'Good answers show you noticed how the same song can create different feelings based on how loud or quiet it is played.'
            }
        ],
        'explainer': '''**Loud and quiet** describe how much sound fills the air. This is called **volume**. When you turn up the volume, you hear more sound. When you turn it down, you hear softer sound. Every song can be played loud or quiet, and it changes how the song feels!

**Loud music** fills the room with strong sound. It reaches your ears with power. Loud music might make you feel excited, energetic, or strong. Think of a trumpet blaring or drums pounding—these are loud! Loud can be fun and thrilling. A celebration or a parade is often loud. When something is loud, everyone can hear it easily.

**Quiet music** uses softer sounds. It is gentle and does not fill as much space. Quiet music might make you feel calm, peaceful, or cozy. A lullaby is quiet. A whispered song is quiet. Someone playing very softly on a piano is quiet. Quiet music invites you to listen closely and pay attention.

Here is something amazing: **the same song can sound completely different if you play it loud one time and quiet another time!** If you sing "Twinkle, Twinkle, Little Star" very loudly, it feels bold and strong. If you sing the same song very quietly, it feels gentle and dreamy. Musicians use loud and quiet to create different feelings and tell different stories with the same piece of music.

In your daily life, you hear loud and quiet sounds all the time. A car horn is loud. A whisper is quiet. Rain on the window is gentle and quiet. Thunder is loud and powerful. Learning to notice loud and quiet helps you listen to music better and understand all the sounds around you!
'''
    },
    'high-and-low-pitch': {
        'questions': [
            {
                'question': 'What is a high sound?',
                'type': 'multiple-choice',
                'options': ['A sound that is very loud', 'A sound that goes up high in your ears, like a bird singing', 'A sound that comes from big instruments', 'A sound that lasts a long time'],
                'answer': 1,
                'explanation': 'A high sound is one that is up in your ears, like a bird singing, a whistle, or a small bell. Your voice goes high when you squeak!'
            },
            {
                'question': 'What is a low sound?',
                'type': 'multiple-choice',
                'options': ['A sound that is quiet', 'A sound that goes down low, like a big drum or a growl', 'A sound that is short', 'A sound that is sad'],
                'answer': 1,
                'explanation': 'A low sound is deep and down in your ears, like a big drum, a foghorn, or a growl. When you make your voice low, it sounds like you are in a big cave!'
            },
            {
                'question': 'A high sound and a low sound can be equally loud.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! You can have a loud high sound and a quiet high sound. You can also have a loud low sound and a quiet low sound. Pitch and volume are different!'
            },
            {
                'question': 'Only big instruments can make low sounds.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'You can make low sounds with your own voice by making it deep and growly! Small instruments can also make low sounds depending on how you play them.'
            },
            {
                'question': 'Make a high sound with your voice and then a low sound. Can you make them at different volumes?',
                'type': 'short-answer',
                'answer': 'Make a high squeak quietly and a high squeak loudly. Make a deep growl quietly and a deep growl loudly.',
                'explanation': 'Good answers show that you can control pitch and volume separately. The same pitch can be loud or quiet, or high or low.'
            }
        ],
        'explainer': '''**High and low pitch** are about where a sound sits in your ears. High sounds go "up" in your ears, and low sounds go "down" in your ears. This is called the **pitch** of a sound. Every sound has a pitch, whether it is music or just something you hear in the world!

A **high sound** feels like it is reaching up into your ears. When you hear a bird singing or a whistle blowing, that is a high sound! If you make your voice very squeaky or squeak like a mouse, that is a high pitch. A small bell or a xylophone often makes high sounds. High sounds seem bright and sparkly to your ears. When you go "eeeee" with your voice, you are making a high sound.

A **low sound** feels deep and down in your ears. A big drum makes a low sound. A foghorn is low. When you growl or make your voice very deep and rumbling, you are making a low sound. Bass singers have very low voices. A tuba in a band makes low sounds. Low sounds seem warm and rich to your ears. When you go "ooooo" in the deepest voice you can, you are making a low sound.

**Here is an important idea: pitch and volume are different!** You can make a high sound that is loud, or a high sound that is quiet. You can make a low sound that is loud, or a low sound that is quiet. A tiny bell might be high and quiet. A trumpet might be high and loud. A distant drum might be low and quiet. A bass drum might be low and loud. All these combinations are possible!

When you listen to music, you will hear many different pitches all happening together. The high sounds make a sparkly feel. The low sounds make a solid, warm feel. Together, all the pitches create a beautiful and interesting sound. Try singing a simple song like "Mary Had a Little Lamb." Now sing the same song, but make your voice as high and squeaky as you can. Then sing it as low and deep as you can. The melody stays the same, but your pitch changed, so it sounds different!
'''
    },
    'moving-to-music': {
        'questions': [
            {
                'question': 'What happens to your body when you hear music you like?',
                'type': 'multiple-choice',
                'options': ['Your body stays completely still', 'Your body wants to move', 'You immediately sit down', 'Nothing happens to your body'],
                'answer': 1,
                'explanation': 'Music makes your body want to move! You might sway, dance, clap, or tap your feet. Music and movement go together naturally.'
            },
            {
                'question': 'How can you match your movements to the music?',
                'type': 'multiple-choice',
                'options': ['Move however you want, ignoring the music', 'Listen to how fast or slow the music is, and move at the same speed', 'Only move your hands', 'Never move your whole body'],
                'answer': 1,
                'explanation': 'Listen to the music and let your body respond! If the music is fast, move quickly. If it is slow, move slowly. If it feels happy, move with joy!'
            },
            {
                'question': 'There is only one correct way to dance to any piece of music.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'Everyone can dance differently! Some people jump, some sway, some skip. Your own way of moving is the right way for you. Music invites movement, not just one movement.'
            },
            {
                'question': 'Moving to music helps you understand the music better.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'When you move to music, you feel it in your body. You understand the speed, the mood, and the rhythm better when you move along with it!'
            },
            {
                'question': 'Listen to a song and show me three different ways you can move to it.',
                'type': 'short-answer',
                'answer': 'Examples: skip, clap, sway; jump, spin, wave; march, bounce, stretch.',
                'explanation': 'Good answers show three different movements. It does not matter what the movements are—the idea is to let the music inspire your body to move in different ways.'
            }
        ],
        'explainer': '''**Moving to music** is one of the most natural and fun things your body can do! When you hear music, your body wants to respond. You might tap your foot, sway your hips, clap your hands, jump, or dance. Music and movement are deeply connected. They happen together!

When you **listen to music**, your ears hear the beat, the speed, and the feeling of the song. Your body picks up on these things and wants to move. If the music is fast and bouncy, your body wants to move fast and bounce. If the music is slow and gentle, your body wants to move slowly and gently. This happens naturally—you do not have to think about it. Your body just knows!

**Every person can move to music in their own way.** There is no one right way to dance. Some people like to jump and spin. Some people like to sway gently. Some people like to march like soldiers. Some people like to bounce or wave their arms. All of these ways of moving are wonderful! The important thing is to listen to the music and let your body respond in a way that feels good to you.

**Moving to music helps you understand the music better.** When you move along with the beat, you feel the rhythm in your bones. When you move fast or slow, you experience the tempo in your muscles. When you move in a happy or sad way, you feel the mood of the music in your heart. Your whole body becomes a listener, not just your ears!

Music gives your body permission to move freely and express itself. It is joyful, it is healthy, and it is creative. Whether you are dancing in your living room, marching in a parade, or swaying at a concert, moving to music is a way of celebrating what you hear and what you feel. Try it right now—turn on a song and let your body dance!
'''
    },
    'call-and-response': {
        'questions': [
            {
                'question': 'What is a "call" in call-and-response music?',
                'type': 'multiple-choice',
                'options': ['A phone call', 'A sound or phrase that someone starts with', 'The last part of a song', 'A loud noise'],
                'answer': 1,
                'explanation': 'A call is a sound or phrase that someone sings or plays first. It is like saying "Hello!" and then waiting for someone to say "Hello!" back.'
            },
            {
                'question': 'What do you do when it is your turn in call-and-response?',
                'type': 'multiple-choice',
                'options': ['Stay quiet and listen', 'Copy or answer what was just played or sung', 'Sing a different song', 'Clap as loudly as you can'],
                'answer': 1,
                'explanation': 'When someone calls, you respond! You echo what they did, or you answer with your own idea. It is like a musical conversation.'
            },
            {
                'question': 'Call-and-response is like a conversation where people take turns making sounds.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! One person calls, another person responds. Back and forth, back and forth. It is a musical conversation, just like talking!'
            },
            {
                'question': 'In call-and-response, everyone sings or plays at exactly the same time.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No, people take turns! One person or group calls, then the other person or group responds. The timing creates the back-and-forth pattern.'
            },
            {
                'question': 'Have a call-and-response conversation with a friend using sounds. You call, they respond, then you respond again.',
                'type': 'short-answer',
                'answer': 'Example: You say "Hello!" and friend says "Hello!" back. Or you clap twice and friend claps twice back. Or you sing "La la la" and friend sings "La la la" back.',
                'explanation': 'Good answers show understanding of the back-and-forth pattern where one person starts and the other person replies or copies.'
            }
        ],
        'explainer': '''**Call-and-response** is a musical game where people take turns making sounds. One person (or group) makes a sound or sings a phrase—that is the "call." Then another person (or group) echoes it or answers with their own sound—that is the "response." Back and forth, back and forth. It is like a musical conversation!

The **call** is the first part. Someone sings a phrase, plays a rhythm, or makes a sound. They are inviting others to participate. The call might be as simple as "Hello!" or a short musical phrase, or a rhythmic clap. The call says "It is your turn now!"

The **response** is what comes next. The other person or group echoes the same sound, or they answer with something new. If you hear "Hello!" you might say "Hello!" back. If you hear a rhythm clapped out, you might clap the same rhythm back. If someone sings "La la la," you sing "La la la" back. The response is your turn to make a sound!

**Call-and-response builds listening and turn-taking skills.** You have to listen closely to know when your turn is coming. You have to wait for your turn instead of jumping in. You have to try to match what you heard, or create something that answers the call. These are important skills for music, conversation, and playing together!

Call-and-response happens everywhere! In church, a leader might sing a phrase and everyone sings back. In parades, musicians call back and forth. In playground games, children might chant back and forth. In Africa and the Caribbean, call-and-response is a big part of music and celebration. Try it yourself: call out "One, two, three!" and have a friend call back "Four, five, six!" Or clap a rhythm and have a friend clap it back. Call-and-response is joyful, social, and fun!
'''
    },
    'echoing-patterns': {
        'questions': [
            {
                'question': 'What does it mean to echo a pattern?',
                'type': 'multiple-choice',
                'options': ['To ignore the pattern', 'To copy what someone did, in the same way', 'To make the pattern faster', 'To sing a song loudly'],
                'answer': 1,
                'explanation': 'When you echo a pattern, you copy it. If someone claps three times, you clap three times in the same way. You are repeating exactly what you heard!'
            },
            {
                'question': 'Which is an example of an echoing pattern?',
                'type': 'multiple-choice',
                'options': ['Teacher: clap, clap. Student: stays quiet.', 'Teacher: clap, clap. Student: clap, clap.', 'Teacher: claps. Student: sings.', 'Teacher: claps fast. Student: claps slow.'],
                'answer': 1,
                'explanation': 'When the teacher claps twice, and the student claps twice in the same way, that is echoing! You are copying the exact pattern you heard.'
            },
            {
                'question': 'Echoing patterns helps you remember what you heard.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! When you echo a pattern, you practice listening carefully and remembering what you heard. This makes your memory stronger!'
            },
            {
                'question': 'You have to change the pattern when you echo it to make it better.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No, when you echo, you copy it the same way! You are not supposed to change it. That is what echoing means.'
            },
            {
                'question': 'I will give you a sound pattern. You echo it back to me exactly.',
                'type': 'short-answer',
                'answer': 'Clap, snap, clap. (The student copies these three sounds in the same order and timing.)',
                'explanation': 'Good answers show that you can listen to a pattern and repeat it exactly as you heard it. The order and speed should match.'
            }
        ],
        'explainer': '''**Echoing patterns** means copying a sequence of sounds or actions exactly as you hear them. When someone makes a pattern—like clap, clap, snap, clap—you echo it back: clap, clap, snap, clap. You are repeating exactly what you heard. It is like being a musical mirror!

**A pattern** is a sequence of sounds or actions that repeat or have a special order. Patterns are everywhere in music and in life. A pattern might be: tap, tap, clap. Or: loud, quiet, loud, quiet. Or: fast, fast, slow, fast. When a pattern repeats, it becomes familiar and you can remember it.

When you **echo a pattern**, you listen very carefully. You hear the first sound, the second sound, the third sound. You remember the order. You remember whether the sounds were fast or slow, loud or quiet, high or low. Then you try to copy it exactly. This takes concentration! But it is a wonderful way to build your listening skills and your memory.

**Echoing patterns is like playing a musical game.** Someone makes a pattern, and you are the echo machine! If you are the echo machine, you copy exactly. If someone is the echo machine and you make the pattern, you get to test whether they copied you well. Back and forth, you practice listening, remembering, and repeating.

Echoing patterns helps you become a better musician and listener. Professional musicians do this all the time. When you echo patterns, you are training your brain to notice details in sound, remember what you hear, and recreate it. These skills help you learn to sing songs, play instruments, and understand music. Start simple with patterns of two or three sounds, and as you get better, try longer and more complex patterns!
'''
    },
    'environmental-sounds': {
        'questions': [
            {
                'question': 'What are environmental sounds?',
                'type': 'multiple-choice',
                'options': ['Sounds made only by instruments', 'Sounds you hear in the world around you, like birds, cars, and rain', 'Sounds made only by people talking', 'Sounds that happen only at night'],
                'answer': 1,
                'explanation': 'Environmental sounds are all the sounds in nature and the world—birds singing, wind blowing, cars driving, water running. These are sounds everywhere!'
            },
            {
                'question': 'Where can you find environmental sounds?',
                'type': 'multiple-choice',
                'options': ['Only in music lessons', 'Only indoors in your house', 'Outside in the world and indoors too—everywhere!', 'Only in zoos'],
                'answer': 2,
                'explanation': 'Environmental sounds are all around you, everywhere you go! Outside and inside. In your home, in the park, on the street, at the beach.'
            },
            {
                'question': 'Environmental sounds are just noise and not real music.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'Environmental sounds can be used to make music! A composer can record bird sounds and use them in a song. Rain sounds can be beautiful and musical.'
            },
            {
                'question': 'You can learn about music by listening to environmental sounds.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Environmental sounds teach you about pitch, rhythm, volume, and patterns. A bird call has a rhythm. Wind has different volumes. These are all musical ideas!'
            },
            {
                'question': 'List three environmental sounds you hear in your daily life.',
                'type': 'short-answer',
                'answer': 'Examples: birds chirping, cars honking, wind blowing, water running, rain falling, dogs barking, doors closing, phone ringing.',
                'explanation': 'Good answers show you can identify real sounds from your environment. They should be sounds that happen in nature or in the world around you.'
            }
        ],
        'explainer': '''**Environmental sounds** are all the sounds you hear in the world around you. Birds singing, wind blowing, rain falling, cars driving, doors closing, water running—these are all environmental sounds. They are not instruments and not someone singing words, but they are definitely sounds you can listen to and learn from!

Every place has its own **sound environment**. Outside, you might hear birds, wind, cars, people, and animals. Inside your house, you might hear doors opening and closing, water running, appliances beeping, and footsteps. At the beach, you hear waves and seagulls. In the forest, you hear leaves crunching and insects buzzing. Even quiet places have sounds if you listen carefully!

**Environmental sounds have musical qualities.** A bird call has a high pitch and a rhythm. Rain has soft volume and gentle patterns. A door slamming has a loud, sudden sound. Thunder is very low and powerful. Wind whooshes and changes. When you listen to environmental sounds, you are practicing the same listening skills you use for music—noticing pitch, rhythm, volume, and emotion.

**Musicians use environmental sounds in their music.** A composer might record the sound of a thunderstorm and use it in a piece of music. A musician might imitate animal sounds on an instrument. A poet might describe the rhythm of waves crashing. Environmental sounds are all around you, ready to inspire music and creativity!

When you go outside or sit quietly inside, try this: listen for environmental sounds. What do you hear? What is high, and what is low? What is loud, and what is quiet? Does it have a rhythm? These questions help you listen to the musical qualities in the natural world. You will discover that the world is full of music if you listen carefully!
'''
    },
    'familiar-songs': {
        'questions': [
            {
                'question': 'What is a familiar song?',
                'type': 'multiple-choice',
                'options': ['A song you have never heard before', 'A song you know and hear again and again', 'A song that is too long', 'A sad song'],
                'answer': 1,
                'explanation': 'A familiar song is one you already know. You have heard it many times, so you know how it goes. Like "Happy Birthday" or "Twinkle, Twinkle, Little Star."'
            },
            {
                'question': 'Why are familiar songs good for learning?',
                'type': 'multiple-choice',
                'options': ['Because they are boring', 'Because you already know them, so you can focus on other things like pitch or rhythm', 'Because they are always slow', 'Because they have no meaning'],
                'answer': 1,
                'explanation': 'Because you already know a familiar song, you can sing along easily. Then you can pay attention to things like how high or low the notes are, or the beat of the song.'
            },
            {
                'question': 'Familiar songs help you remember words and melodies.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! When you sing a song many times, you remember the words and the tune. Your brain stores them and brings them back when you hear the song again.'
            },
            {
                'question': 'You should only sing new songs and never sing familiar songs again.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'Familiar songs are wonderful to sing again and again! Each time you sing them, you get better. And they bring joy and comfort because you know them so well.'
            },
            {
                'question': 'Tell me your favorite familiar song and why you like it.',
                'type': 'short-answer',
                'answer': 'Example: "Twinkle, Twinkle, Little Star because I like how gentle it sounds and I know all the words."',
                'explanation': 'Good answers include the name of a song you know well and a reason you like it, like how it sounds or how it makes you feel.'
            }
        ],
        'explainer': '''**Familiar songs** are songs you already know. You have heard them many times—maybe hundreds of times! Like "Happy Birthday," "Twinkle, Twinkle, Little Star," or songs you learn in school or at home. These songs feel comfortable and safe because you know exactly how they go.

When a song is **familiar**, your brain remembers it. You remember the words, the tune, and how it feels. When you hear it again, you can sing along without thinking too hard. The song feels like an old friend. This is wonderful because it means you do not have to work to remember it—it just comes naturally to you.

**Familiar songs are perfect for learning music skills.** Because you already know the song, you can pay attention to other things. Maybe you listen for where the notes go high and low. Maybe you clap along to the beat. Maybe you notice how fast or slow it is. Maybe you think about what feelings the song gives you. When the song is familiar, you have space in your brain to notice these musical details.

**Learning familiar songs by singing them again and again** helps your voice get stronger and your memory get better. Each time you sing "Mary Had a Little Lamb," your voice remembers the tune better. Your mouth remembers the words. Your body remembers the rhythm. This is practice, and practice makes things easier and more fun!

Familiar songs also **bring comfort and joy.** When you hear a song you love, it makes you smile. It might remind you of someone you love or a happy time. Familiar songs create feelings of belonging and safety. They are part of your memory and your heart. Sing your familiar songs proudly and joyfully. There is no such thing as singing a familiar song too many times!
'''
    },
    'instruments-you-blow': {
        'questions': [
            {
                'question': 'What are blow instruments?',
                'type': 'multiple-choice',
                'options': ['Instruments you hit', 'Instruments you make sound by blowing air into them', 'Instruments you shake', 'Instruments you strum'],
                'answer': 1,
                'explanation': 'Blow instruments make sound when you blow air into them. Recorders, flutes, trumpets, and whistles are all blow instruments!'
            },
            {
                'question': 'What happens when you blow air into a recorder?',
                'type': 'multiple-choice',
                'options': ['Nothing happens', 'The air makes the instrument vibrate and create sound', 'It makes a loud noise like thunder', 'It breaks the instrument'],
                'answer': 1,
                'explanation': 'When you blow gently into a recorder, the air makes it vibrate and creates a beautiful sound. The sound depends on how hard you blow and which holes you cover.'
            },
            {
                'question': 'All blow instruments sound exactly the same.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! A whistle sounds different from a flute, which sounds different from a trumpet. Each blow instrument has its own special sound.'
            },
            {
                'question': 'You have to blow as hard as possible to play a blow instrument correctly.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! You can blow gently or blow harder to change how loud the sound is. Gentle blowing makes softer sounds. Hard blowing makes louder sounds.'
            },
            {
                'question': 'Make a blow sound with your mouth or find a blow instrument. Show me two different ways to blow it.',
                'type': 'short-answer',
                'answer': 'Blow gently to make a soft sound, and blow harder to make a loud sound. Or blow in two different ways to change the pitch.',
                'explanation': 'Good answers show you understand that how you blow changes the sound—you can make it louder or quieter by blowing harder or softer.'
            }
        ],
        'explainer': '''**Blow instruments** are tools that make sound when you blow air into them. Flutes, recorders, whistles, trumpets, and harmonicas are all blow instruments. When you blow air into them, the air makes the instrument vibrate, and the vibration creates sound!

When you **blow into a recorder or flute**, your breath travels through the instrument and makes something inside vibrate. This vibration creates sound that comes out of the instrument. The sound has a special character that belongs to that instrument—flutes sound flute-y, recorders sound recorder-y. Each blow instrument has its own voice!

**You control the sound by how you blow.** If you blow gently, the sound is soft and quiet. If you blow harder, the sound gets louder and stronger. If you blow in the middle, the sound is medium. You are the one controlling how loud or soft the sound is! This is like controlling the volume with your breath.

**Many blow instruments let you change the pitch by covering holes.** A recorder has holes along its body. When you cover different holes with your fingers, the air travels a different path, and the pitch changes! High pitches happen when certain holes are open. Low pitches happen when other holes are open. This is how you play different notes on the same instrument.

**Blow instruments teach you breath control.** You learn to breathe in a way that makes a steady sound. You learn how much air to use and how fast to push it out. You learn to control your lips and mouth to shape the sound. These skills help you play the instrument better and also help you sing! Try humming through your closed teeth—that is a little bit like blowing into an instrument. Now try blowing through a tissue paper tube. What sounds can you make?
'''
    },
    'instruments-you-shake': {
        'questions': [
            {
                'question': 'What are shake instruments?',
                'type': 'multiple-choice',
                'options': ['Instruments you blow into', 'Instruments that make sound when you shake them', 'Instruments you sit on', 'Instruments that need electricity'],
                'answer': 1,
                'explanation': 'Shake instruments make sound when you shake them back and forth. Maracas, shakers, and rattles are all shake instruments!'
            },
            {
                'question': 'Why does a maraca make sound when you shake it?',
                'type': 'multiple-choice',
                'options': ['Because you blow into it', 'Because little balls or seeds inside hit the sides as you shake it', 'Because you hit it hard', 'Because of magic'],
                'answer': 1,
                'explanation': 'Inside a maraca are little balls or seeds. When you shake the maraca, these things move around and hit the sides, making a clicking, rattling sound!'
            },
            {
                'question': 'You can only shake an instrument in one way—back and forth.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'You can shake in many ways! Back and forth, side to side, up and down, fast, slow, gently, or vigorously. Each way makes a slightly different sound!'
            },
            {
                'question': 'Shake instruments help you learn about rhythm because you control the shaking speed.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! When you shake fast, you create a quick rhythm. When you shake slowly, you create a slow rhythm. Your shaking controls the beat!'
            },
            {
                'question': 'Find something that shakes and makes a sound, or pretend you have a maraca. Shake it slow, then shake it fast.',
                'type': 'short-answer',
                'answer': 'Shake slowly: a gentle, steady shaking sound. Shake fast: a quick, rapid shaking sound with shorter gaps between sounds.',
                'explanation': 'Good answers show you can control the rhythm of the shaking and hear how the speed of shaking changes how the sound feels.'
            }
        ],
        'explainer': '''**Shake instruments** make sound when you shake them back and forth. Maracas, shakers, rattles, tambourines, and rain sticks are all shake instruments. Inside these instruments are little balls, seeds, or beads. When you shake the instrument, these things move around and bump into the sides, creating a clicking, rattling, or jingling sound!

When you **shake a maraca**, you are creating vibration through movement. The faster you shake, the faster the little things inside bump and click. The slower you shake, the slower the sounds come out. You control the rhythm and speed of the sound just by how you shake the instrument!

**Different shaking motions make different sounds.** If you shake back and forth fast, you get a quick "shh-shh-shh-shh" sound. If you shake side to side slowly, you get a "shh... shh... shh" sound. If you shake up and down gently, you get a softer sound. If you shake with energy and speed, you get a louder, more exciting sound. The same instrument can sound completely different depending on how you shake it!

**Shake instruments help you learn rhythm.** When you play a shake instrument, you are practicing keeping a steady beat or a special pattern. If you want the rhythm to be fast, you shake fast. If you want it to be slow, you shake slowly. Your body learns to feel the rhythm as your hand does the shaking. This is how musicians train their sense of rhythm!

**Shake instruments are fun and easy to play.** Even a very young child can pick up a maraca and make music by shaking it! You do not need lessons or practice to make joyful sounds. But the more you shake, the better you become at controlling the rhythm and the speed. Shake along with songs, create your own patterns, or just enjoy the sound of shaking!
'''
    },
    'instruments-you-strum': {
        'questions': [
            {
                'question': 'What does "strum" mean?',
                'type': 'multiple-choice',
                'options': ['To blow into something', 'To move your fingers across strings quickly and lightly', 'To hit something hard', 'To shake something back and forth'],
                'answer': 1,
                'explanation': 'To strum means to move your fingers or a pick across the strings of an instrument. Guitars and harps are strum instruments!'
            },
            {
                'question': 'Which instrument would you strum?',
                'type': 'multiple-choice',
                'options': ['A drum', 'A flute', 'A guitar', 'A bell'],
                'answer': 2,
                'explanation': 'A guitar has strings, and you strum across those strings to make sound. That is why it is called a strum instrument!'
            },
            {
                'question': 'When you strum a guitar, different pitches come from different strings.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! A guitar has many strings. Each string is different thickness or length, so each one makes a different pitch when strummed.'
            },
            {
                'question': 'Strum instruments are the same as shake instruments.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No, they are different! Strum instruments have strings. You move your fingers across them. Shake instruments have things inside that rattle. You shake them.'
            },
            {
                'question': 'Show me how you would strum an imaginary guitar or harp.',
                'type': 'short-answer',
                'answer': 'Move your fingers across an imaginary set of strings, moving across them like a brushing motion.',
                'explanation': 'Good answers show a brushing or sweeping motion with the fingers, as if moving across strings from top to bottom or side to side.'
            }
        ],
        'explainer': '''**Strum instruments** are instruments with strings that you play by moving your fingers or a pick across the strings. Guitars, harps, and ukuleles are strum instruments. When you strum, your fingers or a pick brush quickly across the strings, and the strings vibrate to make sound!

A **guitar has many strings stretched tightly across its body.** Each string is a different thickness or is tuned to a different tightness. Because each string is different, each one makes a different pitch when you strum it. When you strum all the strings together, you hear many different pitches at once, creating a full, rich sound. When you strum individual strings, you hear different notes.

**Strumming creates rhythm and melody.** When musicians strum a guitar in a pattern—down, down, up, down, up—they create a rhythm that listeners can feel. When they move to different strings in a special order, they create a melody. A simple strum can make a song, and a complex strum pattern can make a song come alive!

**Different strumming styles make different sounds.** If you strum fast and energetic, the sound is bright and lively. If you strum gently and slowly, the sound is soft and peaceful. If you strum hard, the sound is loud and strong. If you strum delicately, the sound is tender. The same guitar can sound completely different depending on how you strum it!

**Learning to strum takes practice, but it is very rewarding.** When you learn to strum, you learn to coordinate your hands—one hand holds or positions the guitar, and the other hand does the strumming. You learn to feel the rhythm in your body and make your hands match it. Strum instruments have been played for thousands of years, making beautiful music all over the world. If you ever pick up a guitar or harp, you are joining a tradition of musicians going back through history!
'''
    },
    'lullabies': {
        'questions': [
            {
                'question': 'What is a lullaby?',
                'type': 'multiple-choice',
                'options': ['A fast, loud song', 'A gentle song sung to help someone fall asleep', 'A funny song with jokes', 'A song about animals'],
                'answer': 1,
                'explanation': 'A lullaby is a soft, gentle song meant to help babies and children fall asleep. Lullabies are slow and soothing, with simple melodies.'
            },
            {
                'question': 'How should a lullaby sound?',
                'type': 'multiple-choice',
                'options': ['Fast and jumpy', 'Loud and exciting', 'Slow, gentle, and calm', 'Scary and mysterious'],
                'answer': 2,
                'explanation': 'A lullaby should sound slow, gentle, and calm. It should help someone relax and feel sleepy, not energized or startled!'
            },
            {
                'question': 'Lullabies have been sung to babies for thousands of years.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Lullabies are ancient. Parents and caregivers have sung lullabies to help children sleep all over the world and throughout history.'
            },
            {
                'question': 'Lullabies are only for babies who cannot understand words.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'While lullabies are often sung to babies, older children and even adults can enjoy the calming, gentle feeling of a lullaby!'
            },
            {
                'question': 'Sing or hum a lullaby, or describe one you know. What makes it feel calm and sleepy?',
                'type': 'short-answer',
                'answer': 'Example: "Twinkle, Twinkle, Little Star is slow and gentle. It has simple, easy words. It is quiet and soothing."',
                'explanation': 'Good answers mention qualities like slow tempo, gentle sound, simple words, or quiet volume that make a lullaby calming.'
            }
        ],
        'explainer': '''**A lullaby is a gentle song sung to help someone fall asleep.** Parents and caregivers have sung lullabies to babies for thousands and thousands of years. All around the world, in every culture, people sing soft, soothing songs to help children rest. Lullabies are one of the oldest and most universal kinds of music!

**Lullabies sound calm and gentle.** They are slow, not fast. The sounds are soft, not loud. The melody is simple and easy to follow. The words are usually simple, sometimes repeated over and over. Everything about a lullaby is designed to make you feel peaceful and sleepy. When you hear a lullaby, your body relaxes, your breathing slows down, and your mind settles into a quiet, dreamy place.

**The rhythm of a lullaby is like a heartbeat or rocking motion.** Many lullabies have a gentle, steady beat that feels like being rocked back and forth in a cradle. This rhythm is soothing because it reminds us of safety and care. When you sing a lullaby, you might sway or rock gently. The rhythm and the motion work together to create a calm feeling.

**Common lullabies are sung all over the world.** "Twinkle, Twinkle, Little Star" is a lullaby. "Rock-a-bye, Baby" is a lullaby. "Brahms' Lullaby" is a famous lullaby that parents sing. Many cultures have their own special lullabies with words in their own languages, but they all share the same purpose—to calm and comfort.

**Listening to or singing a lullaby can help you relax even if you are not trying to sleep.** If you feel worried, angry, or upset, a lullaby can help calm your feelings. The gentle music soothes your heart. Some people listen to lullabies when they feel stressed, sick, or sad. Lullabies bring comfort because they remind us of being cared for and loved. They say silently: "It is okay. You are safe. Rest now."
'''
    },
    'music-and-feelings': {
        'questions': [
            {
                'question': 'How does music connect to feelings?',
                'type': 'multiple-choice',
                'options': ['Music has no connection to feelings', 'Music can make you feel happy, sad, calm, or energized', 'Music only affects your ears', 'Feelings and music are completely separate'],
                'answer': 1,
                'explanation': 'Music can change how you feel! Happy music might make you smile and want to dance. Calm music might make you feel peaceful. Music and feelings go together!'
            },
            {
                'question': 'What kind of music might help you feel calm?',
                'type': 'multiple-choice',
                'options': ['Fast, loud, bouncy music', 'Slow, gentle, soft music', 'Loud music with lots of noises', 'Scary, intense music'],
                'answer': 1,
                'explanation': 'Slow, gentle, soft music—like lullabies or peaceful instrumental music—helps you feel calm and relaxed. Your body and mind respond to the gentleness.'
            },
            {
                'question': 'Music can change your mood and how you feel.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Music is powerful. If you are sad and you listen to happy music, you might start to feel happier. If you are energized and you listen to calm music, you might slow down.'
            },
            {
                'question': 'Everyone feels the same way when they hear the same music.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Music touches people differently. One person might feel happy listening to a song while another person feels sad. Your own feelings and memories shape how music affects you.'
            },
            {
                'question': 'Tell me about a song that makes you feel something special. What do you feel, and why do you think the music makes you feel that way?',
                'type': 'short-answer',
                'answer': 'Example: "Happy Birthday makes me happy because it is a celebration and reminds me of people I love at my party."',
                'explanation': 'Good answers name a song and describe a feeling it creates, and explain why (the speed, the sound, or a memory connected to it).'
            }
        ],
        'explainer': '''**Music and feelings are deeply connected.** When you listen to music, it does not just go into your ears. It goes into your heart and touches your emotions. Music can make you happy, sad, calm, excited, peaceful, or energized. Music is one of the most powerful ways we express and experience feelings!

**Happy music makes you want to smile and move.** When you hear bright, fast, bouncy music with high sounds, your body responds. You might want to dance, jump, or sing along. Your face might smile without you even thinking about it. Happy music fills your body with energy and joy. It is like the music is saying "Celebrate! Have fun! Be joyful!"

**Calm music helps you relax and feel peaceful.** When you hear slow, soft, gentle music, your breathing slows down. Your muscles relax. Your mind becomes quiet. You feel safe and comfortable. Calm music is like a warm hug. It wraps around you and makes you feel okay, even if you were worried or upset before.

**Sad music helps you feel and express sadness.** Sometimes sad music helps you cry or let out feelings you were holding inside. Sad music says "It is okay to feel sad sometimes. Your feelings matter." Sad music is beautiful because it reminds us that all feelings, even hard ones, are part of being human.

**Your own memories and experiences shape how music makes you feel.** If you heard a song at a birthday party with people you love, that song might always make you feel happy and loved. If you heard a song when you were scared, that song might feel scary to you now. Music is personal. What makes one person happy might make another person feel different. That is okay! Everyone's feelings about music are real and true. When you listen to music, pay attention to how it makes YOU feel. Your feelings are the answer!
'''
    },
    'musical-games': {
        'questions': [
            {
                'question': 'What is a musical game?',
                'type': 'multiple-choice',
                'options': ['A game with no music', 'A game that uses music, singing, or sounds', 'A game you play alone', 'A game that is only for adults'],
                'answer': 1,
                'explanation': 'A musical game uses music, singing, or sounds as part of playing. Freeze dance, Simon Says with sounds, and singing games are all musical games!'
            },
            {
                'question': 'What do musical games teach you?',
                'type': 'multiple-choice',
                'options': ['Nothing important', 'Listening skills, rhythm, turn-taking, and having fun together', 'Only how to be loud', 'Only how to be quiet'],
                'answer': 1,
                'explanation': 'Musical games teach you to listen, feel rhythm, take turns, work together, and have fun! You learn music skills while playing and laughing.'
            },
            {
                'question': 'Musical games are a fun way to practice music and learn together.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Games make learning music fun. When you play musical games, you are practicing music skills without even thinking you are "learning"—you are just having fun!'
            },
            {
                'question': 'Musical games are only for children who are already good musicians.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Musical games are for everyone, whether you are just starting out or you are experienced. They are meant to be joyful and playful for all!'
            },
            {
                'question': 'Describe a musical game you know or could create. What makes it fun?',
                'type': 'short-answer',
                'answer': 'Example: "Freeze Dance is fun because you get to dance and also there is a surprise when the music stops and you have to freeze."',
                'explanation': 'Good answers describe a game and explain what makes it enjoyable, like the element of surprise, movement, music, or playing together.'
            }
        ],
        'explainer': '''**Musical games are games that use music, singing, or sounds as part of the fun.** They might be silly, competitive, creative, or just joyful. Freeze dance is a musical game. So is Simon Says with sounds, or singing in a circle and passing around a toy. Musical games turn learning into play!

**Musical games teach important skills without feeling like work.** When you play freeze dance, you are practicing listening and reacting quickly. When you play a clapping game, you are practicing rhythm and taking turns. When you sing in a circle, you are practicing your voice and working together with others. But it does not feel like practicing—it feels like playing and having fun!

**Games bring people together through music and sound.** Musical games are social. You play with friends or family. You take turns. You listen to each other. You laugh together. Music and games together create joy and connection. When you play a musical game, you are not alone—you are part of a group making sounds and having fun together.

**There are musical games from all over the world.** Some cultures have traditional games played for hundreds of years. Some are simple games you can create yourself. You can play musical games with instruments, with your voice, with your body, or with objects around you. The possibilities are endless! The most important thing is that everyone is having fun and listening to the music together.

**You can create your own musical games!** With a friend or group, think of a music idea and turn it into a game. Maybe you pass a musical instrument around a circle and everyone plays it when it comes to them. Maybe you make up silly sounds and everyone copies them. Maybe you dance in different ways when you hear different songs. The best musical games are the ones that make you laugh, move, listen, and feel connected to the people you are playing with!
'''
    },
    'musical-moods': {
        'questions': [
            {
                'question': 'What is a musical mood?',
                'type': 'multiple-choice',
                'options': ['How loud a song is', 'The feeling or atmosphere that music creates', 'How long a song lasts', 'The name of a song'],
                'answer': 1,
                'explanation': 'A musical mood is the feeling or atmosphere that music creates. Happy, sad, calm, energetic, playful, and mysterious are all musical moods.'
            },
            {
                'question': 'Which describes a playful mood in music?',
                'type': 'multiple-choice',
                'options': ['Slow and serious', 'Fast, bouncy, and fun with silly or teasing sounds', 'Very quiet and still', 'Dark and scary'],
                'answer': 1,
                'explanation': 'Playful music is fast and bouncy with fun sounds that make you want to smile, laugh, or dance. It is lighthearted and silly!'
            },
            {
                'question': 'The same song can create different moods depending on how fast or slow it is played.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! A familiar song played fast might sound happy and energetic. The same song played slowly might sound calm or thoughtful. Tempo changes the mood!'
            },
            {
                'question': 'Every person feels the same mood when they hear the same song.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! People experience music differently. One person might feel happy hearing a song while another person feels peaceful. Moods are personal!'
            },
            {
                'question': 'Listen to a piece of music and describe the mood you feel. What in the music created that mood?',
                'type': 'short-answer',
                'answer': 'Example: "The music sounds mysterious because it is slow with low sounds and there are long pauses that make me wonder what will happen next."',
                'explanation': 'Good answers name a mood and explain what musical elements created it (speed, pitch, volume, instruments, or other qualities).'
            }
        ],
        'explainer': '''**Musical moods are the feelings or atmosphere that music creates.** Happy, sad, calm, energetic, playful, mysterious, scary, and loving are all different musical moods. The same piece of music might create different moods for different people, but every song has a mood that the composer and musicians create.

**Composers and musicians create moods using different musical elements.** They choose the tempo (fast or slow). They choose the pitch (high or low sounds). They choose the volume (loud or soft). They choose the instruments. They choose the rhythm and patterns. All of these choices work together to create a specific mood. It is like painting with sound!

**Happy, energetic moods use fast tempos and bright sounds.** When you hear happy music, it often uses quick beats, high pitches, and major scales that sound cheerful. Your body responds by wanting to move and smile. The music is like sunshine in your ears!

**Calm, peaceful moods use slow tempos and gentle sounds.** When you hear calm music, it often uses slow beats, soft volume, and soothing instruments. Your body responds by relaxing and your mind becomes quiet. The music is like a warm blanket around you.

**It is amazing to discover that the same song can create different moods depending on how it is played.** A lullaby played with a fast, bouncy tempo would not sound like a lullaby anymore! A celebration song played very slowly would not feel like a celebration. Tempo and mood are deeply connected. As you listen to more music, you will become better at recognizing moods. You will notice what in the music creates the feeling you experience. You might even want to create your own moods by playing instruments or singing in different ways!
'''
    },
    'repeating-sounds-and-patterns': {
        'questions': [
            {
                'question': 'What is a pattern in music?',
                'type': 'multiple-choice',
                'options': ['A loud noise', 'A sequence of sounds that repeats or has a special order', 'A colorful picture', 'A fast song'],
                'answer': 1,
                'explanation': 'A pattern is sounds in a special order that happens again and again. Like clap, clap, snap repeated over and over. Patterns help organize music!'
            },
            {
                'question': 'Why are patterns important in music?',
                'type': 'multiple-choice',
                'options': ['They make music boring', 'They help us remember, predict, and feel the structure of music', 'They are only in children\'s music', 'Patterns are not important'],
                'answer': 1,
                'explanation': 'Patterns help you predict what comes next in a song. When you hear a pattern repeat, your brain remembers it and expects it to happen again. Patterns make music feel organized and satisfying!'
            },
            {
                'question': 'When you hear a familiar pattern, you can predict what comes next.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Your brain learns patterns. If you hear clap, clap, snap, clap, clap, snap, you can guess that the next sounds will be clap, clap, snap again!'
            },
            {
                'question': 'All songs have the exact same pattern from beginning to end.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Songs might use a pattern as the foundation, but they usually change it, add to it, or surprise you with something new sometimes.'
            },
            {
                'question': 'Create a simple sound pattern and then repeat it several times. Can a friend predict what comes next?',
                'type': 'short-answer',
                'answer': 'Example: Clap, snap, clap, snap, clap, snap. After hearing it twice, a friend can guess the next sounds are clap, snap.',
                'explanation': 'Good answers show a clear repeating pattern that someone else can learn and predict after hearing it a couple times.'
            }
        ],
        'explainer': '''**Repeating patterns in music are sequences of sounds that happen again and again.** A pattern might be a rhythm like clap, clap, snap. It might be a melody that repeats. It might be a combination of high and low sounds that happens over and over. Patterns are everywhere in music!

**Patterns help organize music and make it easier to remember.** When you hear a pattern repeat, your brain stores it and learns it. The next time the pattern comes, you recognize it! You can even sing along or continue the pattern yourself. Patterns are like the skeleton of a song—they give structure and shape to the music.

**Your brain loves patterns and predicts what comes next.** Once you learn that a pattern is clap, clap, snap, clap, clap, snap, when you hear "clap, clap," your brain immediately thinks "snap!" Your mind is already anticipating the next sound. This is a wonderful part of how we listen to and understand music. We are always predicting, and patterns help us do that!

**Simple melodies often use repeating patterns.** Think of "Mary Had a Little Lamb." If you know the first phrase, you can recognize it when it repeats. Think of "Happy Birthday." The same melody pattern comes back and helps you feel like you are on a familiar journey. Repeating patterns in melodies make them satisfying and easy to learn.

**The rhythm of songs usually has repeating patterns too.** A steady beat is like a pattern that keeps going: boom, boom, boom, boom. A rhythm might be: ta-ta-ta, rest, ta-ta, rest. When the rhythm pattern repeats, you can move along with it or clap along with it. Musicians use patterns like these to keep everything organized and working together. Patterns are the foundation of music! Watch for them, listen for them, and you will understand music better.
'''
    },
    'rhythm-with-body': {
        'questions': [
            {
                'question': 'What is body rhythm?',
                'type': 'multiple-choice',
                'options': ['A type of dance music', 'Using your body to make rhythm by clapping, stomping, or tapping', 'A way to tell time', 'Something only dancers do'],
                'answer': 1,
                'explanation': 'Body rhythm means using your body to create rhythm. You can clap your hands, stomp your feet, tap your legs, or pat your chest to make rhythms!'
            },
            {
                'question': 'Which of these is a way to make rhythm with your body?',
                'type': 'multiple-choice',
                'options': ['Clapping your hands', 'Stomping your feet', 'Tapping your legs', 'All of the above'],
                'answer': 3,
                'explanation': 'All of these are ways to make rhythm with your body! Your whole body can make sounds and rhythm. You can use your hands, feet, legs, chest, and more!'
            },
            {
                'question': 'Making rhythm with your body helps you understand music better.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! When you move your body in rhythm with music, you feel the beat, the tempo, and the pattern in your muscles and bones. This deepens your understanding!'
            },
            {
                'question': 'You have to be a good dancer to make rhythm with your body.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Everyone can clap, stomp, tap, and move. You do not need to be a dancer. Just listening and moving along is enough to create body rhythm!'
            },
            {
                'question': 'Create a body rhythm using at least three different body sounds. Show me what you do.',
                'type': 'short-answer',
                'answer': 'Example: Clap, clap, stomp, clap, clap, stomp. Or: tap your legs, pat your chest, clap, tap your legs, pat your chest, clap.',
                'explanation': 'Good answers show combining different body sounds into a pattern or rhythm. The exact sounds matter less than showing you can make multiple sounds with your body.'
            }
        ],
        'explainer': '''**Rhythm with body** means using your own body to create rhythm and sounds. You can clap your hands together, stomp your feet on the ground, tap your legs, pat your chest, snap your fingers, or make any sound with your body. Your body is an instrument!

**Every part of your body can make rhythm.** Your hands can clap loudly or softly, fast or slow. Your feet can stomp in a pattern. Your fingers can snap or tap. Your chest can be patted. Your thighs can be tapped. You can even make sounds with your mouth—clicking, popping, or humming. Your whole body is full of rhythm possibilities!

**Making rhythm with your body is a way to feel music in your bones and muscles.** When you clap along with a song, you are not just hearing the beat—you are feeling it. Your hands know the speed. Your feet know the pattern. Your whole body learns and remembers the music. This is a powerful way to connect with music physically.

**Body rhythm teaches you about steady beats and patterns.** When you clap a steady beat—clap, clap, clap, clap—you are training your sense of rhythm. When you create a pattern like clap, clap, stomp, clap, clap, stomp, you are learning how patterns work. Your body becomes your teacher!

**You do not need to be a dancer or a musician to make body rhythm.** Everyone can clap and stomp. Everyone can tap and pat. Everyone has a body that can move and make sounds. Even very young children and very old people can make body rhythm together. It is one of the most universal and joyful ways to participate in music. Pick a song you love and start clapping, stomping, or tapping. Feel the rhythm in your body. You are now making music with your whole self!
'''
    },
    'rhythm-with-instruments': {
        'questions': [
            {
                'question': 'What is rhythm with instruments?',
                'type': 'multiple-choice',
                'options': ['Playing instruments as quietly as possible', 'Using instruments to create rhythm and patterns', 'Only for professional musicians', 'Something that takes years to learn'],
                'answer': 1,
                'explanation': 'Rhythm with instruments means using instruments like drums, shakers, or xylophones to create rhythm and patterns. Even simple instruments can make wonderful rhythms!'
            },
            {
                'question': 'Which instruments are good for practicing rhythm?',
                'type': 'multiple-choice',
                'options': ['Only expensive instruments', 'Drums, shakers, xylophones, and other hitting or shaking instruments', 'Only guitars', 'You cannot practice rhythm with instruments'],
                'answer': 1,
                'explanation': 'Drums, shakers, maracas, xylophones, triangles, and other percussion instruments are perfect for learning rhythm. They are easy to use and make satisfying sounds!'
            },
            {
                'question': 'You can play the same rhythm slowly or quickly on an instrument.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! The rhythm pattern stays the same, but if you play faster, the music feels energetic. If you play slower, it feels calm. Speed changes how the rhythm feels!'
            },
            {
                'question': 'It is hard for children to make rhythm with simple instruments.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Children can easily make rhythm with shakers, drums, and other instruments. Simple instruments are perfect for learning rhythm and having fun!'
            },
            {
                'question': 'Pick an instrument or something you can hit, shake, or tap. Create a rhythm pattern and play it twice.',
                'type': 'short-answer',
                'answer': 'Example: Hit-hit-tap-rest, hit-hit-tap-rest. Or: shake-shake-pause-shake, shake-shake-pause-shake.',
                'explanation': 'Good answers show a clear pattern played on an instrument, repeated at least once so the pattern is recognizable.'
            }
        ],
        'explainer': '''**Rhythm with instruments** means using percussion instruments to create and practice rhythm. When you hit a drum, shake a maraca, or tap on a xylophone in a special pattern, you are making rhythm with instruments. Instruments help you feel rhythm and learn how to organize sounds into patterns!

**Percussion instruments are perfect for learning rhythm.** Drums, shakers, xylophones, triangles, and wooden blocks all make it easy to create clear rhythms. You can control when the sound happens and how strong it is. With instruments, you can create rhythm without needing to know how to read music or play complicated melodies. Just make a pattern and play it!

**When you play rhythm with an instrument, you train your sense of timing and coordination.** Your brain has to know what sound comes next. Your hands have to know when to hit or shake. You are teaching your whole self to understand rhythm and keep a steady beat. Over time, this becomes easier and more natural. Your body starts to know rhythms without you having to think hard about it!

**Rhythm patterns on instruments can be fast or slow, loud or soft, simple or complex.** A simple rhythm for a young child might be: hit-hit-rest-hit. A more complex rhythm might be: hit-tap-shake-snap-rest-hit. You can start with simple patterns and gradually make them more interesting as you practice. And the same pattern sounds different if you play it fast versus slow!

**Playing rhythm together with others is special.** When you sit in a circle with friends or family and everyone plays a rhythm on different instruments, it creates something beautiful. Everyone's rhythm fits together like a puzzle. The combined sounds become a bigger, richer rhythm that is more interesting than any one person playing alone. That is how bands and orchestras work! Start with a simple rhythm on any instrument and discover the joy of playing together!
'''
    },
    'same-and-different-sounds': {
        'questions': [
            {
                'question': 'What does it mean to listen for same and different sounds?',
                'type': 'multiple-choice',
                'options': ['Ignoring all sounds', 'Noticing whether sounds are alike or not alike', 'Listening only to loud sounds', 'Listening only to quiet sounds'],
                'answer': 1,
                'explanation': 'It means paying close attention and noticing when sounds match each other or when they are different. A piano sound and a violin sound are different. Two piano sounds can be the same!'
            },
            {
                'question': 'How are a bird chirping and a dog barking different sounds?',
                'type': 'multiple-choice',
                'options': ['They sound exactly alike', 'They have different pitches, volumes, and qualities', 'There is no difference', 'They are the same sound with different names'],
                'answer': 1,
                'explanation': 'A bird chirp is usually high and quick. A dog bark is usually lower and louder. They are very different sounds made by different animals in different ways!'
            },
            {
                'question': 'You can hear that two instruments playing the same note at the same time sound the same.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Two instruments playing the same pitch together blend in a certain way, and you can tell they are the same note. Your ears can match sounds!'
            },
            {
                'question': 'Every sound is completely different from every other sound.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Some sounds are very similar. Two bells can sound very much alike. Two children humming the same tune sound similar. Our ears can find both similarities and differences.'
            },
            {
                'question': 'Listen to two sounds I make. Tell me if they are the same or different.',
                'type': 'short-answer',
                'answer': 'Compare the sounds: "These are the same because they both sound like a high note" or "These are different because one is high and one is low."',
                'explanation': 'Good answers show that you noticed specific qualities (pitch, loudness, timbre) that are the same or different between the two sounds.'
            }
        ],
        'explainer': '''**Same and different sounds** are concepts you discover by listening carefully. Some sounds match each other—they sound alike. Some sounds are different—they sound different from each other. Learning to hear these similarities and differences makes you a better listener!

**Sounds can be the same in different ways.** Two bells might sound very similar in pitch and tone. Two children humming the same tune make similar sounds. Two people saying the word "hello" sound similar but still unique. You can train your ear to notice when sounds match or are similar.

**Sounds can be different in different ways.** A drum sound is different from a whistle sound. A high note is different from a low note. A loud sound is different from a quiet sound. A bird chirp is different from a car honk. The world is full of different sounds, and each one has its own character!

**Learning to hear same and different sounds helps you understand music better.** When you listen to a song, you might notice that a melody repeats—that is hearing "same" sounds in a pattern. You might notice that a verse is different from a chorus—that is hearing how things change. You might notice that two instruments sound different even when they play the same note—that teaches you about tone quality.

**You can practice listening for same and different sounds in your daily life.** Listen to two different birds singing—how are their calls different? Listen to two car honks—are they the same or different? Listen to your parents' voices—can you tell them apart? Listen to two songs—which parts sound the same, and which sound different? The more you practice, the more you become aware of the amazing variety and similarity in the sounds around you. Your ears are your teachers!
'''
    },
    'singing-along': {
        'questions': [
            {
                'question': 'What does "singing along" mean?',
                'type': 'multiple-choice',
                'options': ['Singing by yourself in silence', 'Singing with a song that is playing, trying to match it', 'Not singing at all', 'Singing a completely different song'],
                'answer': 1,
                'explanation': 'Singing along means singing with a song while it is playing. You try to match the words, melody, and rhythm of the song.'
            },
            {
                'question': 'What is one good thing about singing along with a song?',
                'type': 'multiple-choice',
                'options': ['It makes the song stop', 'It helps you learn the song and have fun at the same time', 'It makes the song quieter', 'There is nothing good about it'],
                'answer': 1,
                'explanation': 'Singing along helps you learn words and melodies while you enjoy the music. It is fun, social, and educational at the same time!'
            },
            {
                'question': 'You should only sing along if you know every word and note perfectly.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! You can sing along even if you only know some words or you make mistakes. Trying and singing together is the fun part!'
            },
            {
                'question': 'Singing along helps you remember the words and melody of a song.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! When you sing along, you practice the words and tune over and over. Your voice and your memory learn the song together!'
            },
            {
                'question': 'Sing along with a familiar song. Tell me how it felt to sing with the music.',
                'type': 'short-answer',
                'answer': 'Example: "It felt fun and I liked hearing my voice with the song. I felt like I was part of the music."',
                'explanation': 'Good answers mention positive feelings like joy, connection, fun, or a sense of participation in the music.'
            }
        ],
        'explainer': '''**Singing along** means singing with a song while it is playing. You hear the song, and you sing the words and melody at the same time. It is one of the most joyful and natural ways to participate in music! When people sing together, something magical happens.

**When you sing along with a song, you are joining in with the music.** You are not just listening anymore—you are making sounds and becoming part of the music. Your voice blends with the recording or with other people singing. You feel the rhythm in your body and in your voice. You become a musician, even if you do not think of yourself as one!

**Singing along helps you learn songs.** Each time you sing along with a song, you practice the words and the melody. Your voice learns the pitch. Your mouth learns the words. Your brain stores the tune. After you sing along with a song many times, you start to know it. You can sing parts of it without the recording. The song becomes part of you!

**There is no such thing as singing "perfectly" when you sing along.** You might forget a word and make something up. You might not hit every note exactly right. You might go slightly off-pitch. That is okay! Singing along is not about being perfect. It is about participating, enjoying, and learning. Everyone does it—even professional singers sing along with songs they love!

**Singing along is how humans have participated in music for thousands of years.** In churches, synagogues, and mosques, people sing along with prayers and hymns. At concerts, fans sing along with their favorite artists. In homes all over the world, families sing songs together. When you sing along, you are part of a huge human tradition of making music together. Do not worry about being perfect. Just open your mouth and sing! The joy is in the participation, not the perfection.
'''
    },
    'sound-and-silence': {
        'questions': [
            {
                'question': 'What is silence in music?',
                'type': 'multiple-choice',
                'options': ['A type of loud sound', 'The absence of sound; when there is nothing to hear', 'A sad mood', 'A long song'],
                'answer': 1,
                'explanation': 'Silence is when there is no sound at all. It is the opposite of sound. In music, silence is just as important as sound!'
            },
            {
                'question': 'Why is silence important in music?',
                'type': 'multiple-choice',
                'options': ['It is not important at all', 'It gives listeners a break and makes the sounds that come after stand out more', 'It makes music boring', 'It is a mistake'],
                'answer': 1,
                'explanation': 'Silence is a rest in the music. It lets listeners breathe and listen. When silence ends, the next sound seems more noticeable and special!'
            },
            {
                'question': 'Every moment of music should have a sound; silence is a waste of time in music.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Silence in music is intentional and important. It is not wasted time. It is part of the music! Silence creates contrast and makes listeners pay attention.'
            },
            {
                'question': 'Sound and silence work together to create interesting music.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Music is made up of both sound and silence. Without silence, all the sounds blend together and nothing stands out. With silence, the sounds have meaning and impact!'
            },
            {
                'question': 'Make a simple pattern using sound and silence. Example: one sound, then a pause, then two sounds, then a pause.',
                'type': 'short-answer',
                'answer': 'Example: Clap (pause) clap-clap (pause) clap (pause) clap-clap-clap. The pauses are silence; the claps are sound.',
                'explanation': 'Good answers show a clear pattern where sound and silence alternate in a recognizable way. The pauses are as important as the claps!'
            }
        ],
        'explainer': '''**Sound and silence are the two ingredients of music.** Sound is the noises you hear—notes, words, rhythms, instruments. Silence is the absence of sound—the pauses and rests in between. Both are equally important! Together, they create music that is interesting and meaningful.

**When there is sound, your ears hear something.** You hear a note, a word, a rhythm, an instrument. Sounds fill the air with vibrations. Your ears receive these vibrations and your brain interprets them as music, words, or noise. Sounds are active and present.

**When there is silence, your ears hear nothing.** The air stops vibrating. It is quiet. But silence is not empty or meaningless. Silence gives your ears a break. It gives your brain time to process what it just heard. Silence creates space and room for meaning. A pause in a song makes you wonder what comes next. It creates anticipation!

**Sound and silence together create rhythm and interest.** A song that was all sound with no rests would be boring and tiring. A pattern like: clap, clap, pause, clap has rhythm because of both the sounds and the silence. The silence is part of the pattern! Musicians call rests "notes of silence," because they are just as important as the notes of sound.

**In your daily life, silence and sound are always balancing each other.** Listen to a conversation—people talk (sound) and then pause (silence) so others can speak. Listen to a heartbeat—boom, silence, boom, silence. Watch waves at the beach—splash (sound), then a quiet moment (silence) before the next wave. Sound and silence are natural partners. In music, a great composer uses both skillfully to create something beautiful. When you listen to music, pay attention to both the sounds and the silences. Notice how the silence makes the next sound feel fresh and new!
'''
    },
    'sound-stories': {
        'questions': [
            {
                'question': 'What is a sound story?',
                'type': 'multiple-choice',
                'options': ['A book you read', 'A story told using sounds and music instead of words', 'A song with lots of words', 'A quiet activity'],
                'answer': 1,
                'explanation': 'A sound story is a story told through sounds, music, and noises instead of words. You hear the sounds and imagine the story in your mind!'
            },
            {
                'question': 'How do you listen to a sound story?',
                'type': 'multiple-choice',
                'options': ['You read it from a book', 'You watch a video', 'You listen carefully and use your imagination to picture what is happening', 'You sing along with words'],
                'answer': 2,
                'explanation': 'You listen closely to the sounds and let your imagination create the pictures and story. Your mind paints the scene based on what your ears hear!'
            },
            {
                'question': 'Sound stories help you imagine and be creative.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! When you listen to a sound story, your imagination is working hard. You create mental pictures based on the sounds. This is creative and fun!'
            },
            {
                'question': 'In a sound story, happy events always have fast, loud music.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! A happy event might have soft, gentle music if it is joyful and peaceful. A scary event might have slow, creepy sounds. The music matches the feeling, not just fast or loud.'
            },
            {
                'question': 'Create a simple sound story. Use sounds to tell a short tale. What happens in your story?',
                'type': 'short-answer',
                'answer': 'Example: "A bird wakes up (chirp), walks around the forest (rustling), finds food (crunch), and flies away (swoosh)."',
                'explanation': 'Good answers use different sounds to represent different events in a simple story. The sounds help the listener understand and imagine what is happening.'
            }
        ],
        'explainer': '''**Sound stories are stories told using sounds, music, and noises instead of words.** A sound story might start with the sound of a door creaking open. Then you hear footsteps. Then thunder crashes. Your imagination fills in the details and creates the story in your mind. You become the storyteller because you interpret the sounds!

**When you listen to a sound story, your imagination is your most important tool.** Your ears hear the sounds—maybe a gentle tinkling bell, then bigger bells, then silence. Your mind creates the pictures and the story. Maybe the sounds tell about a little mouse waking up, looking for breakfast, finding cheese, and going back to sleep. Someone else might imagine a completely different story from the same sounds! That is the magic of sound stories.

**Sound stories use all the music ideas you have learned.** They use high and low pitch to help you imagine tall and short things. They use fast and slow tempo to show action or rest. They use loud and quiet volume to show importance or secrets. They use different instruments and environmental sounds to create different moods and scenes. Sound stories put all these musical ideas together to tell a story!

**Sound stories help you connect sounds with emotions and imagination.** When you hear scary sounds—maybe low rumbles, sudden crashes, creepy silence—you feel tension and wonder what is happening. When you hear peaceful sounds—maybe gentle rain, soft instruments, warm melody—you feel calm and safe. The sounds guide your emotions, and your emotions guide your imagination.

**You can create your own sound stories!** Think of a simple adventure. What sounds would you use at the beginning? What sounds for the middle? What for the end? Use your voice, objects around you, instruments, or recorded sounds. Tell a story with sound! You might create a story about a raindrop falling from the sky, or a butterfly exploring a garden, or a knight on an adventure. Sound stories are creativity and music and imagination all mixed together!
'''
    },
    'taking-turns-with-music': {
        'questions': [
            {
                'question': 'What does "taking turns with music" mean?',
                'type': 'multiple-choice',
                'options': ['Playing music alone', 'Taking turns making sounds or playing so everyone gets a chance to participate', 'Singing in silence', 'Not playing at all'],
                'answer': 1,
                'explanation': 'Taking turns with music means one person plays or sings, then they stop and another person plays or sings. Back and forth, everyone gets a turn!'
            },
            {
                'question': 'Why is taking turns important in music?',
                'type': 'multiple-choice',
                'options': ['It is not important', 'It teaches you to listen, wait your turn, and work together', 'It makes music boring', 'Only some people need to take turns'],
                'answer': 1,
                'explanation': 'Taking turns teaches you important skills like listening while you wait, knowing when your turn is coming, and cooperating with others. Everyone gets heard!'
            },
            {
                'question': 'When you are waiting for your turn in a musical performance, you should not pay attention.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! When you are waiting for your turn, you should listen carefully. Listening to others helps you know when your turn is coming and helps the whole group play together.'
            },
            {
                'question': 'Taking turns helps everyone feel like they are part of the music group.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! When everyone gets a turn, everyone feels included and valued. Everyone contributes to the music. That builds community and joy!'
            },
            {
                'question': 'With a friend, take turns making sounds or singing. First you make sounds, then your friend does, and so on.',
                'type': 'short-answer',
                'answer': 'Example: You clap three times, friend claps three times, you make a vocal sound, friend makes a vocal sound, etc.',
                'explanation': 'Good answers show a clear back-and-forth pattern where one person finishes and another person starts. It shows understanding of waiting and listening.'
            }
        ],
        'explainer': '''**Taking turns with music** means one person plays, sings, or makes sounds, and then another person gets a turn. Back and forth, round and round. Everyone gets time to make music and everyone gets time to listen. It is like a musical conversation!

**When you take turns with music, you learn to listen while you wait.** You wait for your turn, listening to what the other person is doing. You learn to anticipate when your turn is coming. You listen for the moment when they finish and it becomes your time to play. This teaches you attention and patience. Your ears are always working, even when you are not the one making the sounds!

**Taking turns teaches you about rhythm and cooperation.** When you and a friend take turns making sounds, you create a back-and-forth rhythm together. You have to know when to start and when to stop. You have to pay attention to each other. You are working together, not just doing your own thing. This is collaboration!

**Orchestra and band musicians take turns all the time.** In a band, the trumpet section plays a part, then the drum section plays, then everyone plays together. In a conversation with music, one person or group solos while others listen, then everyone trades places. Musicians must be great listeners because they are constantly listening to know their part and when to play it.

**Taking turns with music is a way to be fair and kind.** When everyone gets a turn, everyone feels valued and heard. Nobody is left out. When you listen to someone else's turn, you are showing respect. When it is your turn, you are showing the group what you can do. Taking turns teaches that music is something we make together, and every voice and every instrument matters. In your family or friend group, try taking turns making musical sounds. Let everyone be heard. Watch how good it feels when everyone participates!
'''
    },
    'long-and-short-sounds': {
        'questions': [
            {
                'question': 'What is a long sound?',
                'type': 'multiple-choice',
                'options': ['A sound that happens once', 'A sound that lasts for a while', 'A very loud sound', 'A high-pitched sound'],
                'answer': 1,
                'explanation': 'A long sound is one that you hold or that keeps going for a while. Like a long "oooooo" or holding a note on an instrument.'
            },
            {
                'question': 'What is a short sound?',
                'type': 'multiple-choice',
                'options': ['A sound that is quiet', 'A sound that happens quickly and stops right away', 'A sound that is in the morning', 'A sound that is scary'],
                'answer': 1,
                'explanation': 'A short sound is quick—it happens and stops almost immediately. Like a knock, a tap, a handclap, or a short "huh!" sound.'
            },
            {
                'question': 'Music can have both long and short sounds mixed together.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Most music has both long and short sounds. Long sounds might be held notes, and short sounds might be quick beats or notes. They work together!'
            },
            {
                'question': 'A long sound is always louder than a short sound.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! You can have a long, quiet sound. You can have a short, loud sound. How long a sound lasts and how loud it is are different things.'
            },
            {
                'question': 'Make a long sound with your voice, then a short sound. Can you make them different?',
                'type': 'short-answer',
                'answer': 'Long sound: "oooooo" (hold for a few seconds). Short sound: "huh!" (quick and stop). Or make them high and low, loud and quiet.',
                'explanation': 'Good answers show you can control how long a sound lasts. You understand the difference between holding a sound and making it quick.'
            }
        ],
        'explainer': '''**Long and short sounds are about how much time a sound lasts.** A long sound continues for a while—you can count while it is happening. A short sound happens quickly and is over almost immediately. In music, these two types of sounds create rhythm and interest!

**A long sound is one you can hold or that takes time to finish.** When you sing a long "aaaahhhhh," that is a long sound. When you hold a note on a trumpet for several seconds, that is a long sound. When a bell keeps ringing after you hit it, that is a long sound. Long sounds fill time and space in music. They can feel peaceful, powerful, or dreamy depending on what comes before and after them.

**A short sound happens quickly.** When you clap once, that is a short sound. When you tap a drum quickly, that is a short sound. When you say "pop!" with your voice, that is a short sound. Short sounds are like little bursts of energy. They move music forward. They create quick rhythms and exciting moments.

**Long and short sounds together create rhythm and excitement.** A pattern like: long-short-short-long-short creates interest because it mixes things up. Your ears do not know what is coming next. If all the sounds were long, the music might feel slow and drawn out. If all the sounds were short, it might feel frantic. The mix of long and short creates a satisfying rhythm!

**You can hear long and short sounds in words and in nature.** When you say "hello," that is longer than when you say "hi." When you hear a crack of thunder, that is sometimes short and sometimes long depending on the storm. When a bee buzzes, that is a shorter sound than a train whistle. Pay attention to long and short sounds all around you. Then try making them with your voice or with instruments. Discover how long and short sounds can work together to create music that is interesting and alive!
'''
    },
    'how-instruments-make-sound': {
        'questions': [
            {
                'question': 'What causes an instrument to make sound?',
                'type': 'multiple-choice',
                'options': ['Electricity', 'Vibration—something moves back and forth very fast', 'Magic', 'Paint on the instrument'],
                'answer': 1,
                'explanation': 'Vibration! When you hit a drum, blow a flute, or pluck a string, something vibrates (shakes back and forth super fast). These vibrations create sound!'
            },
            {
                'question': 'How does a drum make sound?',
                'type': 'multiple-choice',
                'options': ['It has magic inside', 'When you hit the drum head, it vibrates and creates sound', 'It only makes sound if you sing', 'Drums cannot actually make sound'],
                'answer': 1,
                'explanation': 'When you hit a drum head, it vibrates up and down very quickly. These vibrations travel through the air and reach your ears as sound!'
            },
            {
                'question': 'All instruments make sound the same way.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Different instruments vibrate in different ways. Drums vibrate because you hit them. Strings vibrate because you pluck or bow them. Flutes vibrate because you blow air through them.'
            },
            {
                'question': 'Vibration is necessary for instruments to make sound.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Without vibration, there would be no sound. All sound comes from something vibrating. Your vocal cords vibrate when you sing!'
            },
            {
                'question': 'Find something that vibrates when you play it (or imagine one). Describe how it vibrates and what sound it makes.',
                'type': 'short-answer',
                'answer': 'Example: "When I tap a drum, the drum head shakes back and forth really fast and makes a deep boom sound."',
                'explanation': 'Good answers describe what vibrates and connect it to the sound that is made. Understanding the vibration helps you understand how all instruments work!'
            }
        ],
        'explainer': '''**All instruments make sound through vibration.** Vibration means something shakes back and forth very, very fast. When you hit a drum, the drum head vibrates. When you pluck a guitar string, the string vibrates. When you blow air into a flute, something inside the flute vibrates. These vibrations are so fast your eyes cannot see them, but your ears hear them as sound!

**When something vibrates, it pushes the air around it.** Imagine a drum vibrating up and down. As it moves up, it pushes air up. As it moves down, it pulls air down. This creates waves of air moving in every direction. These air waves travel to your ears. Your ears receive these waves and your brain interprets them as sound. The vibration of the instrument becomes the sound you hear!

**Different instruments vibrate in different ways, which is why they sound different.** A tiny bell vibrates quickly and creates a high, bright sound. A big bass drum vibrates more slowly and creates a deep, booming sound. A string vibrates one way, and a drum head vibrates another way. Even though they all use vibration, the type of vibration creates different sounds!

**Your own voice is created by vibration too!** Inside your throat are two small folds of skin called vocal cords. When you speak or sing, air passes through them and makes them vibrate. These vibrations travel up through your mouth and out into the world as your voice. You are an instrument! You can feel your vibration by putting your hand on your throat while you hum—you will feel a tickle, which is the vibration of your vocal cords.

**Understanding vibration helps you understand all music.** Sound is vibration. Instruments make vibrations. Your ears receive vibrations and turn them into sound that your brain understands. When you make music, you are creating vibrations. When you listen to music, you are receiving vibrations through your ears. You are connected to music through vibration! Try this: hit a pot with a spoon and watch it wiggle. That wiggling is vibration. That vibration becomes the sound you hear. That is how instruments work!
'''
    },
    'listening-for-sounds': {
        'questions': [
            {
                'question': 'What does "active listening" mean?',
                'type': 'multiple-choice',
                'options': ['Letting sounds wash over you without thinking', 'Paying close attention to what you hear and noticing details', 'Only listening to music you like', 'Covering your ears'],
                'answer': 1,
                'explanation': 'Active listening means really paying attention to sounds. You notice if they are high or low, loud or quiet, near or far. You are engaged and focused!'
            },
            {
                'question': 'What is something you can notice when you listen actively?',
                'type': 'multiple-choice',
                'options': ['Nothing, all sounds are the same', 'Whether a sound is high or low, loud or quiet, fast or slow', 'Only the name of the sound', 'What color the sound is'],
                'answer': 1,
                'explanation': 'When you listen actively, you notice all sorts of details! High or low pitch, loud or quiet, fast or slow, near or far. These details make listening interesting!'
            },
            {
                'question': 'Hearing and listening are exactly the same thing.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Hearing happens automatically—your ears receive sound. Listening requires you to focus and pay attention. Listening is a skill you can improve!'
            },
            {
                'question': 'You can get better at listening by practicing active listening.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! The more you practice paying attention to sounds, the better you become at noticing details. Your listening skill grows stronger with practice!'
            },
            {
                'question': 'Listen to a sound and describe what you notice about it. Is it high or low? Loud or quiet? Fast or slow?',
                'type': 'short-answer',
                'answer': 'Example: "The bird chirp is high and quick. The car horn is low and loud. The wind is medium volume and soft."',
                'explanation': 'Good answers show that you noticed specific qualities of the sound: pitch (high/low), volume (loud/quiet), speed (fast/slow), or other details.'
            }
        ],
        'explainer': '''**Listening for sounds** means paying close attention to what you hear. It is different from just hearing. Your ears automatically hear everything around you, but listening is something you choose to do. When you listen actively, you pay attention and notice details!

When you **hear**, sounds come to your ears without any effort. A dog barks, a car honks, a song plays—your ears automatically receive these sounds. But you might not be thinking about them or noticing what they are. Hearing happens whether you want it to or not.

When you **listen**, you focus your attention on the sounds. You ask yourself: Is this sound high or low? Is it loud or quiet? Is it fast or slow? Where is it coming from? What instrument or thing is making it? These questions help you notice more details. You become an active listener instead of a passive listener!

**Active listening is a skill you can practice and improve.** The more you listen carefully, the better you become at hearing and understanding sounds. You might notice that on your first listen to a song, you hear the main melody. On your second listen, you hear the drums. On your third listen, you hear the background voices. You are hearing more and more details because you are practicing active listening!

**Good listening makes music more enjoyable.** When you listen carefully to a song, you understand it better. You notice how the composer created the feelings. You appreciate the musicianship. You pick up on rhythms, melodies, and harmonies you might have missed before. Try this: listen to a short piece of music twice. The first time, let it play while you do other things. The second time, sit quietly and really focus on the sounds. Notice what you heard the second time that you missed the first time. That is the power of active listening!
'''
    },
    'instrument-families-hit-shake-blow-strum': {
        'questions': [
            {
                'question': 'What are the four families of instruments?',
                'type': 'multiple-choice',
                'options': ['Loud, quiet, fast, slow', 'Hit, shake, blow, strum', 'Red, blue, yellow, green', 'Big, small, pretty, ugly'],
                'answer': 1,
                'explanation': 'The four families are: hit instruments (drums), shake instruments (maracas), blow instruments (flutes), and strum instruments (guitars). Each family makes sound a different way!'
            },
            {
                'question': 'Which family includes instruments you play by moving strings with your fingers?',
                'type': 'multiple-choice',
                'options': ['Hit family', 'Shake family', 'Blow family', 'Strum family'],
                'answer': 3,
                'explanation': 'The strum family! Guitars, harps, and ukuleles are strum instruments. You move your fingers across the strings to make sound.'
            },
            {
                'question': 'Every instrument belongs to one of these four families.',
                'type': 'true-false',
                'answer': True,
                'explanation': 'Yes! Most instruments fit into one of these families based on how they make sound. Understanding the families helps you understand how all instruments work!'
            },
            {
                'question': 'The blow family is the same as the shake family.',
                'type': 'true-false',
                'answer': False,
                'explanation': 'No! Blow instruments need air blown through them. Shake instruments need to be shaken. They work in completely different ways!'
            },
            {
                'question': 'Name one instrument from each family: hit, shake, blow, strum.',
                'type': 'short-answer',
                'answer': 'Hit: drum. Shake: maraca. Blow: flute. Strum: guitar. (Other answers are okay as long as they fit the family.)',
                'explanation': 'Good answers show you can identify an instrument and place it in the correct family based on how it makes sound.'
            }
        ],
        'explainer': '''**The four families of instruments are groups based on how they make sound.** Every instrument in the world fits into one of these four families: hit, shake, blow, or strum. Understanding the families helps you understand how all instruments work!

**The HIT family includes instruments you strike or hit.** Drums, xylophones, triangles, cymbals, and wood blocks are hit instruments. When you hit them, something vibrates and makes sound. The harder you hit, the louder the sound. The softer you tap, the quieter the sound. Hit instruments are ancient—people have been hitting things to make music since the beginning of time!

**The SHAKE family includes instruments that make sound when you shake them.** Maracas, shakers, rattles, and tambourines are shake instruments. Inside these instruments are little balls, seeds, or bells. When you shake them, these things move around and create sound. Shake instruments are wonderful for learning rhythm because your shaking controls the speed!

**The BLOW family includes instruments that use air.** Flutes, recorders, trumpets, whistles, and harmonicas are blow instruments. You blow air into them, and the air makes something inside vibrate and create sound. Blow instruments teach you breath control. You control how loud or soft the sound is by how hard you blow.

**The STRUM family includes instruments with strings.** Guitars, harps, ukuleles, and banjos are strum instruments. You move your fingers across the strings, and the strings vibrate and create sound. Different strings make different pitches. Strum instruments have been played all over the world for thousands of years!

**All four families use vibration to make sound, but they vibrate in different ways.** When you understand these families, you understand how every instrument in the world creates music. You can pick up any instrument and immediately know how to make it sound—hit it, shake it, blow it, or strum it! Try visiting each family. Find or imagine one instrument from each family. Make sounds with them. Notice how different they sound, even though they are all creating vibration and music!
'''
    }
}

def format_questions(questions_data):
    """Format questions as YAML."""
    yaml_content = "```yaml\n"
    for q in questions_data:
        yaml_content += f"- question: \"{q['question']}\"\n"
        yaml_content += f"  type: {q['type']}\n"

        if q['type'] == 'multiple-choice':
            yaml_content += "  options: ["
            yaml_content += ", ".join(f'"{opt}"' for opt in q['options'])
            yaml_content += "]\n"
            yaml_content += f"  answer: {q['answer']}\n"
        elif q['type'] == 'true-false':
            yaml_content += f"  answer: {str(q['answer']).lower()}\n"
        else:  # short-answer
            yaml_content += f"  answer: \"{q['answer']}\"\n"

        yaml_content += f"  explanation: \"{q['explanation']}\"\n\n"

    yaml_content += "```\n"
    return yaml_content

def process_files():
    """Process all 30 markdown files in the music directory."""
    # Convert MSYS path to Windows path for Python
    base_dir = "C:/Users/griff/Projects/griffin/open-knowledge-graph/domains/music/musical-play-and-listening"

    # Get list of markdown files using os.walk
    md_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    md_files = sorted(md_files)

    print(f"Found {len(md_files)} markdown files to process")

    for md_file in md_files:
        topic_id = os.path.splitext(os.path.basename(md_file))[0]
        print(f"Processing: {topic_id}")

        if topic_id not in TOPIC_CONTENT:
            print(f"  WARNING: No content defined for {topic_id}")
            continue

        # Read the file
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if Questions section already exists
        if "## Questions" in content:
            print(f"  SKIPPING: Questions section already exists")
            continue

        # Get the content for this topic
        topic_data = TOPIC_CONTENT[topic_id]
        questions = topic_data['questions']
        explainer = topic_data['explainer']

        # Format the new sections
        questions_section = "## Questions\n\n" + format_questions(questions)
        explainer_section = "## Explainer\n\n" + explainer + "\n"

        # Append to file
        new_content = content.rstrip() + "\n\n" + questions_section + "\n" + explainer_section

        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  SUCCESS: Added Questions and Explainer sections")

    print("\nProcessing complete!")

if __name__ == "__main__":
    process_files()

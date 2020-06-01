import discord


class Glob:
    def __init__(self):
        self.card_image_urls = [
            [
                'https://cdn.discordapp.com/attachments/714679761237966858/714708626190762004/r0.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708627105120317/r1.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708628065615913/r2.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708628883374080/r3.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708629768503316/r4.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708648324104202/r5.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708649326411797/r6.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708650240901120/r7.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708650970841158/r8.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708652120080414/r9.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708670285479966/rd.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708671191580732/rr.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708671891898468/rs.png',
            ],
            [
                'https://cdn.discordapp.com/attachments/714679761237966858/714708672525107200/y0.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708673112571955/y1.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708692053786695/y2.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708692976795678/y3.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708694222241792/y4.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708694864232509/y5.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708695891705897/y6.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708715110006835/y7.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708716074565683/y8.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708716766888006/y9.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708717647429672/yd.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708718603730984/yr.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708736647888916/ys.png',
            ],
            [
                'https://cdn.discordapp.com/attachments/714679761237966858/714708737608253460/g0.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708738484994088/g1.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708739294232586/g2.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708740221304852/g3.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708758638624796/g4.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708759762698281/g5.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708760517672960/g6.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708761402671204/g7.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708762186874930/g8.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708780272713728/g9.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708781103054898/gd.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708782063812648/gr.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708783003074640/gs.png',
            ],
            [
                'https://cdn.discordapp.com/attachments/714679761237966858/714708784186130452/b0.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708801827110952/b1.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708802766897169/b2.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708804020863036/b3.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708804847009803/b4.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708805900042280/b5.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708823620714577/b6.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708824375689226/b7.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708825269075998/b8.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708826393411624/b9.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708827194523688/bd.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708845426901042/br.png',
                'https://cdn.discordapp.com/attachments/714679761237966858/714708846299578418/bs.png',
            ]
        ]
        self.card_image_files = [
            [
                './unocards/r0.png',
                './unocards/r1.png',
                './unocards/r2.png',
                './unocards/r3.png',
                './unocards/r4.png',
                './unocards/r5.png',
                './unocards/r6.png',
                './unocards/r7.png',
                './unocards/r8.png',
                './unocards/r9.png',
                './unocards/rd.png',
                './unocards/rr.png',
                './unocards/rs.png'
            ],
            [
                './unocards/y0.png',
                './unocards/y1.png',
                './unocards/y2.png',
                './unocards/y3.png',
                './unocards/y4.png',
                './unocards/y5.png',
                './unocards/y6.png',
                './unocards/y7.png',
                './unocards/y8.png',
                './unocards/y9.png',
                './unocards/yd.png',
                './unocards/yr.png',
                './unocards/ys.png'
            ],
            [
                './unocards/g0.png',
                './unocards/g1.png',
                './unocards/g2.png',
                './unocards/g3.png',
                './unocards/g4.png',
                './unocards/g5.png',
                './unocards/g6.png',
                './unocards/g7.png',
                './unocards/g8.png',
                './unocards/g9.png',
                './unocards/gd.png',
                './unocards/gr.png',
                './unocards/gs.png'
            ],
            [
                './unocards/b0.png',
                './unocards/b1.png',
                './unocards/b2.png',
                './unocards/b3.png',
                './unocards/b4.png',
                './unocards/b5.png',
                './unocards/b6.png',
                './unocards/b7.png',
                './unocards/b8.png',
                './unocards/b9.png',
                './unocards/bd.png',
                './unocards/br.png',
                './unocards/bs.png'
            ]
        ]
        self.wild_image_urls = [
            'https://cdn.discordapp.com/attachments/714679761237966858/714708847410937916/z.png',
            'https://cdn.discordapp.com/attachments/714679761237966858/714708848283353128/zd.png'
        ]
        self.wild_image_files = [
            './unocards/z.png',
            './unocards/zd.png'
        ]
        self.colours = [
            discord.colour.Color.from_rgb(200, 50, 50),
            discord.colour.Color.from_rgb(200, 200, 50),
            discord.colour.Color.from_rgb(50, 200, 50),
            discord.colour.Color.from_rgb(50, 50, 200),
            discord.colour.Color.from_rgb(200, 200, 200),
            discord.colour.Color.from_rgb(0, 0, 0)
        ]
        self.reaction_emojis = [
            '🅾', '🇦', '🇧', '🇨', '🇩', '🇪',
            '🇫', '🇬', '🇭', '🇮', '🇯', '🇰',
            '🇱', '🇲', '🇳', '🇵', '🇶', '🇷',
        ]
        self.reaction_image_files = [
            './unocards/o2.png',
            './unocards/qa.png',
            './unocards/qb.png',
            './unocards/qc.png',
            './unocards/qd.png',
            './unocards/qe.png',
            './unocards/qf.png',
            './unocards/qg.png',
            './unocards/qh.png',
            './unocards/qi.png',
            './unocards/qj.png',
            './unocards/qk.png',
            './unocards/ql.png',
            './unocards/qm.png',
            './unocards/qn.png',
            './unocards/qp.png',
            './unocards/qq.png',
            './unocards/qr.png'
        ]
        self.join_emoji = '☑'
        self.kick_emoji = '🦿'
        self.draw_emoji = '🅾'
        self.start_emoji = ''

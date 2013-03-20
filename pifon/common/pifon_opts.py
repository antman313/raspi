# pifon_options

# audio options
audio_opts = {
  'trace' : False,
  'level' : 10,
  'attack' : 0,
  'sustain' : 5,
  'respite' : 10,
  'update' : 5
}

audio_desc = {
  'trace' : ('enable level tracing',False,True),
  'level' : ('peak level',1,100),
  'attack' : ('period [1s] of loudness required to start playback',0,10),
  'sustain' : ('period [1s] of silence required to stop playback',0,60),
  'respite' : ('delay [1s] after playback to wait for next',0,60),
  'update' : ('update interval of current peak level [100ms]',1,60)
}

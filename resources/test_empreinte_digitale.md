Testez régulièrement la configuration de votre empreinte digitale
**Testing sites**:
  - https://amiunique.org/
  - https://coveryourtracks.eff.org/ (formerly Panopticlick)
  - https://browserleaks.com/
  - https://fingerprintjs.github.io/fingerprintjs/

**Test checklist**:
  [ ] IP address is VPN/Tor, not real IP
  [ ] WebRTC is disabled (no IP leak)
  [ ] User-Agent matches intended spoof
  [ ] Canvas fingerprint is not unique
  [ ] WebGL fingerprint is not unique
  [ ] Font enumeration is limited
  [ ] Time zone matches expected location
  [ ] Screen resolution is common
  [ ] No plugins detected
  [ ] DNT (Do Not Track) is not set
       (ironically, setting DNT makes you more unique)

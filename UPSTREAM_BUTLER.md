# UPSTREAM_BUTLER.md — proposed implementation-repository handoff

**Status:** PREPARED IN CUMULATIVE PROJECT SET; **NOT COMMITTED** to `RedSigilDelta/butler` or a separate Studio repository. The file is an I0 deliverable candidate, not proof of I0 completion.

## Source and chain of custody

- Canonical upstream: `https://github.com/d4rken-org/butler`.
- Owner's current generic fork: `https://github.com/RedSigilDelta/butler` (`main`).
- Pristine upstream-aligned implementation baseline commit: `cfecd03a1ccbebd022c86841d07f74cd01a28d41`. Historical I0 observation: fork/`upstream`/`origin` aligned at capture; independently recheck the local Git history and remote state before final signing.
- GitHub workflow-only tooling commit at current observed fork HEAD on 2026-10-11: `588251a9347dc5470f8eace29368a21f31750536` — “Add GitHub Actions workflow for FOSS debug build.” Do **not** mistake this for the pristine source baseline.
- Workflow: `.github/workflows/butler-i0-foss-debug.yml`, file blob SHA-1 `2a3840506eb604b5e4016ea19cd7a7e740225d41`, GitHub current contents observed 2026-10-11; manual `workflow_dispatch`, read-only contents permission, Java 21 and Gradle, `app:assembleFossDebug`, `butler-i0-foss-debug` APK artifact.
- At the time of inspection, the fork did not contain `UPSTREAM_BUTLER.md` on `main`. This candidate must be reviewed and applied to the appropriate implementation repo without changing pristine evidence.

## Licensing and rights separation

Butler source code is GPLv3 licensed; preserve relevant copyleft, copyright, notices, change history, license text, and source obligations. The pinned upstream README explicitly excludes original Butler icons, logos, mascots, marketing assets, animations, videos, documentation, Play screenshots/texts and translations from its GPL code grant. Non-code assets and dependencies require per-item rights audit or original/permission-cleared replacement prior to public distribution. Branding as RedSigil∆ does **not** automatically relicense code, fonts, artwork or upstream-derived resources.

For original Studio code, follow the project-specific license map and compatibility review (`LICENSE_POLICY.md` in the cumulative project document set), not a blanket Apache license for GPL-derived components. External Markor v2.16.1 parity is an **implementation** requirement, not proof of code reuse permission for each dependency.

## Build and physical baseline gates

- Run GitHub Actions workflow; retain run URL, conclusion, run/head SHA, jobs/tests, duration, APK artifact name/hash/size, tool versions and logs.
- Verify APK source/variant/signature and install/launch on real Android 16 Galaxy A26. Capture key smoke results and safe installation/coexistence details; do not accidentally overwrite or migrate official Butler data.
- Retain upstream tests/CI limitations and distinguish existing baseline failures from new regressions.
- Audit distributed non-code resources, manifest/provider authorities, third-party licenses, fonts, and all excluded upstream artwork before any public RedSigil∆ distribution.
- Do not begin B0 functional changes before I0 baseline evidence and owner acceptance are complete.

## Program boundaries

Maintain two explicit lines after I0 closure: B0–B15 generic file-manager improvements (with original approved RedSigil∆ branding, final name pending) and I0–I15 Pandoc Studio publishing product (separate identity); shared generic improvements stay separable and upstreamable. All Markor parity, Notes & Tasks, archive IE gates, S0–S10 synchronization rules and unified V1 release gates remain mandatory. The Open Formats & Portability Policy v1.1.0 concerns **project files only**, not application format support.

## Verified source links

- Pristine SHA: `https://github.com/RedSigilDelta/butler/commit/cfecd03a1ccbebd022c86841d07f74cd01a28d41`.
- Tooling SHA: `https://github.com/RedSigilDelta/butler/commit/588251a9347dc5470f8eace29368a21f31750536`.
- Actual workflow: `https://github.com/RedSigilDelta/butler/blob/main/.github/workflows/butler-i0-foss-debug.yml`.
- Pinned upstream exclusions: `https://github.com/d4rken-org/butler/blob/cfecd03a1ccbebd022c86841d07f74cd01a28d41/README.md`.

**Not established:** successful workflow run, APK/build metrics, physical install, actual upstream remote URL in current working checkout, clean local state, source-to-artifact reproducibility, B0 readiness and V1 release readiness. No such approval is implied.

## Fresh empirical evidence (2026-10-11; not yet committed upstream)

- Owner fork newest CI build head `3aa5136edc31684b62e68fd61f11f22615f40d5b` / source Git tree `dbe50a09190195ee71a0ef337dbc6a0593924855`, matched to uploaded GitHub source ZIP.
- CI manual FOSS debug run `38183579397` artifact `11718872024`, inner APK SHA-256 `17fb240c2495e7698aeb9e9a1a6111b30be9b602b524d03fc0d0d4eff2252caa` matched owner APK.
- Owner states physical Galaxy A26 install and launch succeeded; no independent device log.
- The original frozen upstream-aligned baseline remains `cfecd03a1ccbebd022c86841d07f74cd01a28d41`. New build SHA and tooling SHA must not replace its historical role.
- Current `Code tests & eval` has a Robolectric Maven artifact fetch issue; don't imply all tests passed.


## Review-branch evidence amendment — 2026-10-11

Follow the current empirical report `research/implementation/I0_CI_RECERTIFICATION_2026-10-11.md`. The previous-release tag `v0.2.0-beta0` lacks selector key `explorer_navigation_recent`; packaged E2E patch uses `explorer_navigation_home` for 3 assertions. Patch exists only in documentation handoff. Attempt to create review branch via linked GitHub application failed with HTTP 403 (`Resource not accessible by integration`); this file still is **NOT COMMITTED** to repo root and cannot be used as evidence of remote I0 closure. Robolectric unit-test runners continue to fail dependency fetch; device-upgrade E2E rerun not yet done.

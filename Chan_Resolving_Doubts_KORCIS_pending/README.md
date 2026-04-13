# Chan Resolving Doubts / KORCIS Pending

- Work: `禪宗決疑集`
- Priority: high
- Exact lead: KORCIS search results for `禪宗決疑集 / 선종결의집` expose four exact records:
  - `101712358` — `智徹(元) 述`, `金陵刻經處`, `民國 9(1920)刊`
  - `101454226` — `野衲智徹 述`, `[刊寫者未詳]`, `民國 9[1920]`
  - `301543913` — `智徹 述`, `金陵刻經處`, `1920`
  - `139805537` — `智徹 述`, `金陵刻經處`, `1920`
- Lead page: https://www.nl.go.kr/korcis/search/simpleResultList.do?searchCondition=all&searchKeyword=%EC%84%A0%EC%A2%85%EA%B2%B0%EC%9D%98%EC%A7%91
- Holding institution shown in search result: `동국대학교 중앙도서관`
- Availability shown in search result: `원문`, `PDF`, `텍스트`
- Viewer mechanics confirmed:
  - KORCIS detail page for the strongest record: `https://www.nl.go.kr/korcis/search/searchResultDetail.do?searchMenuId=SIMPLE&vdkvgwkey=101712358`
  - Site JavaScript resolves the viewer through `https://viewer.nl.go.kr/nlmivs/viewWonmun_js.jsp?cno=...`
- Additional exact-host check:
  - Google Books API exposes exact 1920 matches including volume id `jQtEAQAAMAAJ` (`禪宗決疑集`, `智徹`, `1920`, UC Berkeley identifier), but marks them `viewability=NO_PAGES`, `publicDomain=false`, and `pdfAvailable=false`.
- Rights concern: this looks promising as an exact witness, but neither the KORCIS detail page nor the viewer bootstrap page exposes an item-level KOGL/open-reuse mark. The National Library of Korea copyright policy says free reuse applies when the library holds the rights or when a public-use marker is provided; KORCIS itself also carries a blanket `Copyright© National Library of Korea. All Rights Reserved.` footer.
- Status: exact witness identified; rights basis unresolved, so not downloaded and not marked acquired.

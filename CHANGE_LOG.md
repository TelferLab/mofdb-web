### v.3.1 (2017-08-31)

Subo requested changes:

1. There are three different catalyst types in the reaction form, REACTION CATALYST CCS, REACTION CATALYST LIGANDS, and REACTION CATALYST MOFs. However, it would be much simpler if we have just one catalyst section and specify which type those catalysts belong to by adding a column.

2. We are currently saving catalyst data in the separated table, then we select its id while we input the catalyst in the reaction form. But there's no point saving these data in the separated table, because there's 1:1 relationship between catalyst and its data. Although, these data are saved in the separated table, we need to input the data and see the data with the corresponding catalyst.

<table class="tg">
  <tr>
    <th class="tg-s6z2">Name<br>        </th>
    <th class="tg-s6z2">Type<br>        </th>
    <th class="tg-s6z2">functional-group<br>        </th>
    <th class="tg-s6z2">amount<br>      </th>
    <th class="tg-s6z2">chirality<br>       </th>
    <th class="tg-s6z2">rate-constant<br>       </th>
    <th class="tg-s6z2">conversion<br>      </th>
    <th class="tg-s6z2">ee<br>      </th>
    <th class="tg-baqh">de<br>      </th>
    <th class="tg-baqh">yield<br>       </th>
  </tr>
  <tr>
    <td class="tg-baqh">L-proline<br>       </td>
    <td class="tg-baqh">CC<br>      </td>
    <td class="tg-baqh">---<br></td>
    <td class="tg-baqh">30<br>      </td>
    <td class="tg-baqh">S<br>       </td>
    <td class="tg-baqh">1.2<br>     </td>
    <td class="tg-baqh">88<br>      </td>
    <td class="tg-baqh">89<br>      </td>
    <td class="tg-baqh">99<br>      </td>
    <td class="tg-baqh">70<br>      </td>
  </tr>
  <tr>
    <td class="tg-baqh">bdc-pro<br>     </td>
    <td class="tg-baqh">Ligand<br>      </td>
    <td class="tg-baqh">proline<br>     </td>
    <td class="tg-baqh">30<br>      </td>
    <td class="tg-baqh">S<br>       </td>
    <td class="tg-baqh">0.8<br>     </td>
    <td class="tg-baqh">60<br>      </td>
    <td class="tg-baqh">70<br>      </td>
    <td class="tg-baqh">88<br>      </td>
    <td class="tg-baqh">50<br>      </td>
  </tr>
  <tr>
    <td class="tg-baqh">MUF-x<br>       </td>
    <td class="tg-baqh">MOF<br>     </td>
    <td class="tg-baqh">proline<br>     </td>
    <td class="tg-baqh">30<br>      </td>
    <td class="tg-baqh">S<br>       </td>
    <td class="tg-baqh">0.74<br>        </td>
    <td class="tg-baqh">55<br>      </td>
    <td class="tg-baqh">60<br>      </td>
    <td class="tg-baqh">77<br>      </td>
    <td class="tg-baqh">40<br>      </td>
  </tr>
</table>


3. The order of attributes in the reaction form should change. Suggested:

| Name | VisualizationReaction | Reactants | Products | Notes | Catalysts | ReactionData |
|------|-----------------------|-----------|----------|-------|-----------|--------------|

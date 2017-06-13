<?php

/**
 * @author zmiller
 */
class ListingsTable extends BaseTable {
    
    public function select($input) {
        $sql = 
<<<EOD
    select * from listings;
EOD;
        return $this->execute($sql);
    }
}
